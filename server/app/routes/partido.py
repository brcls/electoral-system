from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

partido_bp = Blueprint('partido_bp', __name__)


# Rotas para a tabela Partido
@partido_bp.route('/partido', methods=['POST'])
def add_partido():
    data = request.json
    nome = data['nome']
    programa = data['programa']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO partido (nome, programa) VALUES (%s, %s)', (nome, programa))
    conn.commit()
    cur.close()
    return jsonify({"message": "Partido added successfully!"}), 201


@partido_bp.route('/partido', methods=['GET'])
def get_partidos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM partido')
    partidos = cur.fetchall()
    cur.close()
    return jsonify(partidos), 200


@partido_bp.route('/partido/<int:id>', methods=['GET'])
def get_partido(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM partido WHERE id = %s', (id,))
    partido = cur.fetchone()
    cur.close()
    return jsonify(partido), 200 if partido else 404


@partido_bp.route('/partido/<int:id>', methods=['PUT'])
def update_partido(id):
    data = request.json
    nome = data['nome']
    programa = data['programa']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE partido SET nome = %s, programa = %s WHERE id = %s', (nome, programa, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Partido updated successfully!"}), 200


@partido_bp.route('/partido/<int:id>', methods=['DELETE'])
def delete_partido(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM partido WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Partido deleted successfully!"}), 200
