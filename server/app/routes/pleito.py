from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

pleito_bp = Blueprint('pleito_bp', __name__)


# Rotas para a tabela Pleito
@pleito_bp.route('/pleito', methods=['POST'])
def add_pleito():
    data = request.json
    ano = data['ano']
    cargo_id = data['cargo_id']
    candidato_id = data['candidato_id']
    votos_recebidos = data['votos_recebidos']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO pleito (ano, cargo_id, candidato_id, votos_recebidos) VALUES (%s, %s, %s, %s)',
                (ano, cargo_id, candidato_id, votos_recebidos))
    conn.commit()
    cur.close()
    return jsonify({"message": "Pleito added successfully!"}), 201


@pleito_bp.route('/pleito', methods=['GET'])
def get_pleitos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM pleito')
    pleitos = cur.fetchall()
    cur.close()
    return jsonify(pleitos), 200


@pleito_bp.route('/pleito/<int:id>', methods=['GET'])
def get_pleito(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM pleito WHERE id = %s', (id,))
    pleito = cur.fetchone()
    cur.close()
    return jsonify(pleito), 200 if pleito else 404


@pleito_bp.route('/pleito/<int:id>', methods=['PUT'])
def update_pleito(id):
    data = request.json
    ano = data['ano']
    cargo_id = data['cargo_id']
    candidato_id = data['candidato_id']
    votos_recebidos = data['votos_recebidos']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE pleito SET ano = %s, cargo_id = %s, candidato_id = %s, votos_recebidos = %s WHERE id = %s',
                (ano, cargo_id, candidato_id, votos_recebidos, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Pleito updated successfully!"}), 200


@pleito_bp.route('/pleito/<int:id>', methods=['DELETE'])
def delete_pleito(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM pleito WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Pleito deleted successfully!"}), 200
