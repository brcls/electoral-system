from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

processo_judicial_bp = Blueprint('processo_judicial_bp', __name__)


# Rotas para a tabela Processo Judicial
@processo_judicial_bp.route('/processo_judicial', methods=['POST'])
def add_processo_judicial():
    data = request.json
    candidato_id = data['candidato_id']
    status = data['status']
    resultado = data.get('resultado')
    data_inicio = data['data_inicio']
    data_termino = data.get('data_termino')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO processo_judicial (candidato_id, status, resultado, data_inicio, data_termino) 
        VALUES (%s, %s, %s, %s, %s)''',
                (candidato_id, status, resultado, data_inicio, data_termino))
    conn.commit()
    cur.close()
    return jsonify({"message": "Processo Judicial added successfully!"}), 201


@processo_judicial_bp.route('/processo_judicial', methods=['GET'])
def get_processos_judiciais():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM processo_judicial')
    processos_judiciais = cur.fetchall()
    cur.close()
    return jsonify(processos_judiciais), 200


@processo_judicial_bp.route('/processo_judicial/<int:id>', methods=['GET'])
def get_processo_judicial(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM processo_judicial WHERE id = %s', (id,))
    processo_judicial = cur.fetchone()
    cur.close()
    return jsonify(processo_judicial), 200 if processo_judicial else 404


@processo_judicial_bp.route('/processo_judicial/<int:id>', methods=['PUT'])
def update_processo_judicial(id):
    data = request.json
    candidato_id = data['candidato_id']
    status = data['status']
    resultado = data.get('resultado')
    data_inicio = data['data_inicio']
    data_termino = data.get('data_termino')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        UPDATE processo_judicial SET candidato_id = %s, status = %s, resultado = %s, data_inicio = %s, data_termino = %s 
        WHERE id = %s''',
                (candidato_id, status, resultado, data_inicio, data_termino, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Processo Judicial updated successfully!"}), 200


@processo_judicial_bp.route('/processo_judicial/<int:id>', methods=['DELETE'])
def delete_processo_judicial(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM processo_judicial WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Processo Judicial deleted successfully!"}), 200
