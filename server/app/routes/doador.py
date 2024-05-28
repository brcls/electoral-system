from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

doador_bp = Blueprint('doador_bp', __name__)


# Rotas para a tabela Doador
@doador_bp.route('/doador', methods=['POST'])
def add_doador():
    data = request.json
    nome = data['nome']
    tipo = data['tipo']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO doador (nome, tipo) VALUES (%s, %s)', (nome, tipo))
    conn.commit()
    cur.close()
    return jsonify({"message": "Doador added successfully!"}), 201


@doador_bp.route('/doador', methods=['GET'])
def get_doadores():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM doador')
    doadores = cur.fetchall()
    cur.close()
    return jsonify(doadores), 200


@doador_bp.route('/doador/<int:id>', methods=['GET'])
def get_doador(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM doador WHERE id = %s', (id,))
    doador = cur.fetchone()
    cur.close()
    return jsonify(doador), 200 if doador else 404


@doador_bp.route('/doador/<int:id>', methods=['PUT'])
def update_doador(id):
    data = request.json
    nome = data['nome']
    tipo = data['tipo']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE doador SET nome = %s, tipo = %s WHERE id = %s', (nome, tipo, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Doador updated successfully!"}), 200


@doador_bp.route('/doador/<int:id>', methods=['DELETE'])
def delete_doador(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM doador WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Doador deleted successfully!"}), 200
