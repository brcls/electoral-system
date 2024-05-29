from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

equipe_apoio_bp = Blueprint('equipe_apoio_bp', __name__)


# Rotas para a tabela Equipe de Apoio
@equipe_apoio_bp.route('/equipe_apoio', methods=['POST'])
def add_equipe_apoio():
    data = request.json
    candidato_id = data['candidato_id']
    ano = data['ano']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO equipe_apoio (candidato_id, ano) VALUES (%s, %s)', (candidato_id, ano))
    conn.commit()
    cur.close()
    return jsonify({"message": "Equipe de Apoio added successfully!"}), 201


@equipe_apoio_bp.route('/equipe_apoio', methods=['GET'])
def get_equipes_apoio():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('''
        SELECT *, 
        (
            SELECT row_to_json(p)
            FROM candidato c
            JOIN pessoa p ON c.pessoa_id = p.id
            WHERE equipe_apoio.candidato_id = c.id
        ) AS candidato 
        FROM equipe_apoio
    ''')
    equipes_apoio = cur.fetchall()
    cur.close()
    return jsonify(equipes_apoio), 200


@equipe_apoio_bp.route('/equipe_apoio/<int:id>', methods=['GET'])
def get_equipe_apoio(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM equipe_apoio WHERE id = %s', (id,))
    equipe_apoio = cur.fetchone()
    cur.close()
    return jsonify(equipe_apoio), 200 if equipe_apoio else 404


@equipe_apoio_bp.route('/equipe_apoio/<int:id>', methods=['PUT'])
def update_equipe_apoio(id):
    data = request.json
    candidato_id = data['candidato_id']
    ano = data['ano']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE equipe_apoio SET candidato_id = %s, ano = %s WHERE id = %s', (candidato_id, ano, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Equipe de Apoio updated successfully!"}), 200


@equipe_apoio_bp.route('/equipe_apoio/<int:id>', methods=['DELETE'])
def delete_equipe_apoio(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM equipe_apoio WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Equipe de Apoio deleted successfully!"}), 200
