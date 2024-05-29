from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection
from app.routes.candidato import delete_candidato

pessoa_bp = Blueprint('pessoa_bp', __name__)

# Rotas para a tabela Pessoa
@pessoa_bp.route('/pessoa', methods=['POST'])
def add_pessoa():
    data = request.json
    nome = data['nome']
    data_nascimento = data['data_nascimento']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO pessoa (nome, data_nascimento) VALUES (%s, %s)', (nome, data_nascimento))
    conn.commit()
    cur.close()
    return jsonify({"message": "Pessoa added successfully!"}), 201


@pessoa_bp.route('/pessoa', methods=['GET'])
def get_pessoas():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM pessoa')
    pessoas = cur.fetchall()
    cur.close()
    return jsonify(pessoas), 200


@pessoa_bp.route('/pessoa/<int:id>', methods=['GET'])
def get_pessoa(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM pessoa WHERE id = %s', (id,))
    pessoa = cur.fetchone()
    cur.close()
    return jsonify(pessoa), 200 if pessoa else 404


@pessoa_bp.route('/pessoa/<int:id>', methods=['PUT'])
def update_pessoa(id):
    data = request.json
    nome = data['nome']
    data_nascimento = data['data_nascimento']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE pessoa SET nome = %s, data_nascimento = %s WHERE id = %s', (nome, data_nascimento, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Pessoa updated successfully!"}), 200


@pessoa_bp.route('/pessoa/<int:id>', methods=['DELETE'])
def delete_pessoa(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT id FROM candidato WHERE pessoa_id = %s', (id,))
    candidatos = cur.fetchall()
    for candidato in candidatos:
        delete_candidato(candidato[0])

    cur.execute('DELETE FROM pessoa WHERE id = %s', (id,))

    conn.commit()
    cur.close()
    return jsonify({"message": "Pessoa deleted successfully!"}), 200
