from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

candidato_bp = Blueprint('candidato_bp', __name__)


# Rotas para a tabela Candidato
@candidato_bp.route('/candidato', methods=['POST'])
def add_candidato():
    data = request.json
    pessoa_id = data['pessoa_id']
    partido_id = data['partido_id']
    cargo_id = data['cargo_id']
    data_candidatura = data['data_candidatura']
    vice_candidato_id = data.get('vice_candidato_id')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO candidato (pessoa_id, partido_id, cargo_id, data_candidatura, vice_candidato_id) 
        VALUES (%s, %s, %s, %s, %s)''',
                (pessoa_id, partido_id, cargo_id, data_candidatura, vice_candidato_id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Candidato added successfully!"}), 201


@candidato_bp.route('/candidato', methods=['GET'])
def get_candidatos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM candidato')
    candidatos = cur.fetchall()
    cur.close()
    return jsonify(candidatos), 200


@candidato_bp.route('/candidato/<int:id>', methods=['GET'])
def get_candidato(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM candidato WHERE id = %s', (id,))
    candidato = cur.fetchone()
    cur.close()
    return jsonify(candidato), 200 if candidato else 404


@candidato_bp.route('/candidato/<int:id>', methods=['PUT'])
def update_candidato(id):
    data = request.json
    pessoa_id = data['pessoa_id']
    partido_id = data['partido_id']
    cargo_id = data['cargo_id']
    data_candidatura = data['data_candidatura']
    vice_candidato_id = data.get('vice_candidato_id')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''UPDATE candidato SET pessoa_id = %s, partido_id = %s, cargo_id = %s, data_candidatura = %s, 
    vice_candidato_id = %s WHERE id = %s''',
                (pessoa_id, partido_id, cargo_id, data_candidatura, vice_candidato_id, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Candidato updated successfully!"}), 200


@candidato_bp.route('/candidato/<int:id>', methods=['DELETE'])
def delete_candidato(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM candidato WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Candidato deleted successfully!"}), 200
