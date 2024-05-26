from flask import Blueprint, render_template, request, jsonify
from .models import db, Candidato 

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/candidatos', methods=['GET'])
def get_candidatos():
    candidatos = Candidato.query.all()
    return jsonify([candidato.serialize() for candidato in candidatos])

@bp.route('/candidatos', methods=['POST'])
def create_candidato():
    data = request.json
    candidato = Candidato(nome=data['nome'], partido=data['partido'], idade=data['idade'])
    db.session.add(candidato)
    db.session.commit()
    return jsonify({'message': 'Candidato criado com sucesso!'}), 201

@bp.route('/candidatos/<int:id>', methods=['GET'])
def get_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    return jsonify(candidato.serialize())

@bp.route('/candidatos/<int:id>', methods=['PUT'])
def update_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    data = request.json
    candidato.nome = data['nome']
    candidato.partido = data['partido']
    candidato.idade = data['idade']
    db.session.commit()
    return jsonify({'message': 'Candidato atualizado com sucesso!'})

@bp.route('/candidatos/<int:id>', methods=['DELETE'])
def delete_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    db.session.delete(candidato)
    db.session.commit()
    return jsonify({'message': 'Candidato deletado com sucesso!'})
