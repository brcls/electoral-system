from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

participante_equipe_bp = Blueprint('participante_equipe_bp', __name__)


# Rotas para a tabela Participante da Equipe
@participante_equipe_bp.route('/participante_equipe', methods=['POST'])
def add_participante_equipe():
    data = request.json
    pessoa_id = data['pessoa_id']
    equipe_apoio_id = data['equipe_apoio_id']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO participante_equipe (pessoa_id, equipe_apoio_id) VALUES (%s, %s)', (pessoa_id,
                                                                                                 equipe_apoio_id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Participante da Equipe added successfully!"}), 201


@participante_equipe_bp.route('/participante_equipe', methods=['GET'])
def get_participantes_equipe():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM participante_equipe')
    participantes_equipe = cur.fetchall()
    cur.close()
    return jsonify(participantes_equipe), 200


@participante_equipe_bp.route('/participante_equipe/<int:id>', methods=['GET'])
def get_participante_equipe(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM participante_equipe WHERE id = %s', (id,))
    participante_equipe = cur.fetchone()
    cur.close()
    return jsonify(participante_equipe), 200 if participante_equipe else 404


@participante_equipe_bp.route('/participante_equipe/<int:id>', methods=['PUT'])
def update_participante_equipe(id):
    data = request.json
    pessoa_id = data['pessoa_id']
    equipe_apoio_id = data['equipe_apoio_id']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE participante_equipe SET pessoa_id = %s, equipe_apoio_id = %s WHERE id = %s',
                (pessoa_id, equipe_apoio_id, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Participante da Equipe updated successfully!"}), 200


@participante_equipe_bp.route('/participante_equipe/<int:id>', methods=['DELETE'])
def delete_participante_equipe(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM participante_equipe WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Participante da Equipe deleted successfully!"}), 200
