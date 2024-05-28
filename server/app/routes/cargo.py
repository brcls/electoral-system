from flask import Blueprint, request, jsonify
from psycopg2.extras import RealDictCursor
from app.db import get_db_connection

cargo_bp = Blueprint('cargo_bp', __name__)


# Rotas para a tabela Cargo
@cargo_bp.route('/cargo', methods=['POST'])
def add_cargo():
    data = request.json
    nome = data['nome']
    tipo = data['tipo']
    local = data['local']
    quantidade_eleitos = data['quantidade_eleitos']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO cargo (nome, tipo, local, quantidade_eleitos) VALUES (%s, %s, %s, %s)', 
                (nome, tipo, local, quantidade_eleitos))
    conn.commit()
    cur.close()
    return jsonify({"message": "Cargo added successfully!"}), 201


@cargo_bp.route('/cargo', methods=['GET'])
def get_cargos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM cargo')
    cargos = cur.fetchall()
    cur.close()
    return jsonify(cargos), 200


@cargo_bp.route('/cargo/<int:id>', methods=['GET'])
def get_cargo(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM cargo WHERE id = %s', (id,))
    cargo = cur.fetchone()
    cur.close()
    return jsonify(cargo), 200 if cargo else 404


@cargo_bp.route('/cargo/<int:id>', methods=['PUT'])
def update_cargo(id):
    data = request.json
    nome = data['nome']
    tipo = data['tipo']
    local = data['local']
    quantidade_eleitos = data['quantidade_eleitos']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE cargo SET nome = %s, tipo = %s, local = %s, quantidade_eleitos = %s WHERE id = %s', 
                (nome, tipo, local, quantidade_eleitos, id))
    conn.commit()
    cur.close()
    return jsonify({"message": "Cargo updated successfully!"}), 200


@cargo_bp.route('/cargo/<int:id>', methods=['DELETE'])
def delete_cargo(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM cargo WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    return jsonify({"message": "Cargo deleted successfully!"}), 200
