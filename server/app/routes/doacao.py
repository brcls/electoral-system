from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

doacao_bp = Blueprint('doacao_bp', __name__)


# Rotas para a tabela Doação
@doacao_bp.route('/doacao', methods=['POST'])
def add_doacao():
    data = request.json
    doador_id = data['doador_id']
    candidato_id = data['candidato_id']
    valor = data['valor']
    data_doacao = data['data']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO doacao (doador_id, candidato_id, valor, data) VALUES (%s, %s, %s, %s)', 
                (doador_id, candidato_id, valor, data_doacao))
    conn.commit()
    cur.close()
    return jsonify({"message": "Doação added successfully!"}), 201


@doacao_bp.route('/doacao', methods=['GET'])
def get_doacoes():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM doacao')
    doacoes = cur.fetchall()
    cur.close()
    return jsonify(doacoes), 200


@doacao_bp.route('/doacao/<int:id>', methods=['GET'])
def get_doacao(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM doacao WHERE id = %s', (id,))
    doacao = cur.fetchone()
    cur.close()
    return jsonify(doacao), 200 if doacao else 404


@doacao_bp.route('/doacao/<int:id>', methods=['PUT'])
def update_doacao(id):
    data = request.json
    doador_id = data['doador_id']
    candidato_id = data['candidato_id']
    valor = data['valor']
    data_doacao = data['data']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE doacao SET doador_id = %s, candidato_id = %s, valor = %s, data = %s WHERE id = %s', 
                (doador_id, candidato_id, valor, data_doacao, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Doação updated successfully!"}), 200


@doacao_bp.route('/doacao/<int:id>', methods=['DELETE'])
def delete_doacao(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM doacao WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Doação deleted successfully!"}), 200
