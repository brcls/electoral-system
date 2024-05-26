from flask import Blueprint, request, jsonify
from .models import db, Partido, Cargo, Pessoa, Candidato, ProcessoJudicial, EquipeApoio, ParticipanteEquipe, Doador, Doacao, Pleito

bp = Blueprint('api', __name__)

# CRUD for Partido
@bp.route('/partidos', methods=['GET'])
def get_partidos():
    partidos = Partido.query.all()
    return jsonify([partido.serialize() for partido in partidos])

@bp.route('/partidos', methods=['POST'])
def create_partido():
    data = request.json
    partido = Partido(nome=data['nome'], programa=data['programa'])
    db.session.add(partido)
    db.session.commit()
    return jsonify({'message': 'Partido criado com sucesso!'}), 201

@bp.route('/partidos/<int:id>', methods=['GET'])
def get_partido(id):
    partido = Partido.query.get_or_404(id)
    return jsonify(partido.serialize())

@bp.route('/partidos/<int:id>', methods=['PUT'])
def update_partido(id):
    partido = Partido.query.get_or_404(id)
    data = request.json
    partido.nome = data['nome']
    partido.programa = data['programa']
    db.session.commit()
    return jsonify({'message': 'Partido atualizado com sucesso!'})

@bp.route('/partidos/<int:id>', methods=['DELETE'])
def delete_partido(id):
    partido = Partido.query.get_or_404(id)
    db.session.delete(partido)
    db.session.commit()
    return jsonify({'message': 'Partido deletado com sucesso!'})


# CRUD for Cargo
@bp.route('/cargos', methods=['GET'])
def get_cargos():
    cargos = Cargo.query.all()
    return jsonify([cargo.serialize() for cargo in cargos])

@bp.route('/cargos', methods=['POST'])
def create_cargo():
    data = request.json
    cargo = Cargo(nome=data['nome'], tipo=data['tipo'], local=data['local'], quantidade_eleitos=data['quantidade_eleitos'])
    db.session.add(cargo)
    db.session.commit()
    return jsonify({'message': 'Cargo criado com sucesso!'}), 201

@bp.route('/cargos/<int:id>', methods=['GET'])
def get_cargo(id):
    cargo = Cargo.query.get_or_404(id)
    return jsonify(cargo.serialize())

@bp.route('/cargos/<int:id>', methods=['PUT'])
def update_cargo(id):
    cargo = Cargo.query.get_or_404(id)
    data = request.json
    cargo.nome = data['nome']
    cargo.tipo = data['tipo']
    cargo.local = data['local']
    cargo.quantidade_eleitos = data['quantidade_eleitos']
    db.session.commit()
    return jsonify({'message': 'Cargo atualizado com sucesso!'})

@bp.route('/cargos/<int:id>', methods=['DELETE'])
def delete_cargo(id):
    cargo = Cargo.query.get_or_404(id)
    db.session.delete(cargo)
    db.session.commit()
    return jsonify({'message': 'Cargo deletado com sucesso!'})


# CRUD for Pessoa
@bp.route('/pessoas', methods=['GET'])
def get_pessoas():
    pessoas = Pessoa.query.all()
    return jsonify([pessoa.serialize() for pessoa in pessoas])

@bp.route('/pessoas', methods=['POST'])
def create_pessoa():
    data = request.json
    pessoa = Pessoa(nome=data['nome'], data_nascimento=data['data_nascimento'])
    db.session.add(pessoa)
    db.session.commit()
    return jsonify({'message': 'Pessoa criada com sucesso!'}), 201

@bp.route('/pessoas/<int:id>', methods=['GET'])
def get_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    return jsonify(pessoa.serialize())

@bp.route('/pessoas/<int:id>', methods=['PUT'])
def update_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    data = request.json
    pessoa.nome = data['nome']
    pessoa.data_nascimento = data['data_nascimento']
    db.session.commit()
    return jsonify({'message': 'Pessoa atualizada com sucesso!'})

@bp.route('/pessoas/<int:id>', methods=['DELETE'])
def delete_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    db.session.delete(pessoa)
    db.session.commit()
    return jsonify({'message': 'Pessoa deletada com sucesso!'})


# CRUD for Candidato
@bp.route('/candidatos', methods=['GET'])
def get_candidatos():
    candidatos = Candidato.query.all()
    serialize = []
    for candidato in candidatos:
        pessoa = Pessoa.query.get_or_404(candidato.pessoa_id)
        vice_candidato = None if candidato.vice_candidato_id == None else Candidato.query.get(candidato.vice_candidato_id)  
        partido = Partido.query.get_or_404(candidato.partido_id)
        cargo = Cargo.query.get_or_404(candidato.cargo_id)
        equipe_de_apoio = Cargo.query.get_or_404(candidato.cargo_id)

        participantes_equipe = ParticipanteEquipe.query.filter_by(equipe_apoio_id=equipe_de_apoio.id).all()
        serialized_participantes_equipe = [Pessoa.query.get_or_404(participante.pessoa_id).serialize() for participante in participantes_equipe]

        processos = ProcessoJudicial.query.filter_by(candidato_id=candidato.id).all()
        serialized_processos = [processo.serialize() for processo in processos]

        doacoes = Doacao.query.filter_by(candidato_id=candidato.id).all()
        serialized_doacoes = [doacao.serialize() for doacao in doacoes]

        serialize.append(candidato.serialize_candidate(pessoa, vice_candidato, partido, cargo, equipe_de_apoio, serialized_participantes_equipe, serialized_processos, serialized_doacoes))

    return jsonify(serialize)

@bp.route('/candidatos', methods=['POST'])
def create_candidato():
    data = request.json
    candidato = Candidato(pessoa_id=data['pessoa_id'], partido_id=data['partido_id'], cargo_id=data['cargo_id'], data_candidatura=data['data_candidatura'], vice_candidato_id=data.get('vice_candidato_id'))
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
    candidato.pessoa_id = data['pessoa_id']
    candidato.partido_id = data['partido_id']
    candidato.cargo_id = data['cargo_id']
    candidato.data_candidatura = data['data_candidatura']
    candidato.vice_candidato_id = data.get('vice_candidato_id')
    db.session.commit()
    return jsonify({'message': 'Candidato atualizado com sucesso!'})

@bp.route('/candidatos/<int:id>', methods=['DELETE'])
def delete_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    db.session.delete(candidato)
    db.session.commit()
    return jsonify({'message': 'Candidato deletado com sucesso!'})


# CRUD for ProcessoJudicial
@bp.route('/processos_judiciais', methods=['GET'])
def get_processos_judiciais():
    processos = ProcessoJudicial.query.all()
    return jsonify([processo.serialize() for processo in processos])

@bp.route('/processos_judiciais', methods=['POST'])
def create_processo_judicial():
    data = request.json
    processo = ProcessoJudicial(candidato_id=data['candidato_id'], status=data['status'], resultado=data['resultado'], data_inicio=data['data_inicio'], data_termino=data.get('data_termino'))
    db.session.add(processo)
    db.session.commit()
    return jsonify({'message': 'Processo judicial criado com sucesso!'}), 201

@bp.route('/processos_judiciais/<int:id>', methods=['GET'])
def get_processo_judicial(id):
    processo = ProcessoJudicial.query.get_or_404(id)
    return jsonify(processo.serialize())

@bp.route('/processos_judiciais/<int:id>', methods=['PUT'])
def update_processo_judicial(id):
    processo = ProcessoJudicial.query.get_or_404(id)
    data = request.json
    processo.candidato_id = data['candidato_id']
    processo.status = data['status']
    processo.resultado = data['resultado']
    processo.data_inicio = data['data_inicio']
    processo.data_termino = data.get('data_termino')
    db.session.commit()
    return jsonify({'message': 'Processo judicial atualizado com sucesso!'})

@bp.route('/processos_judiciais/<int:id>', methods=['DELETE'])
def delete_processo_judicial(id):
    processo = ProcessoJudicial.query.get_or_404(id)
    db.session.delete(processo)
    db.session.commit()
    return jsonify({'message': 'Processo judicial deletado com sucesso!'})


# CRUD for EquipeApoio
@bp.route('/equipes_apoio', methods=['GET'])
def get_equipes_apoio():
    equipes = EquipeApoio.query.all()
    return jsonify([equipe.serialize() for equipe in equipes])

@bp.route('/equipes_apoio', methods=['POST'])
def create_equipe_apoio():
    data = request.json
    equipe = EquipeApoio(candidato_id=data['candidato_id'], ano=data['ano'])
    db.session.add(equipe)
    db.session.commit()
    return jsonify({'message': 'Equipe de apoio criada com sucesso!'}), 201

@bp.route('/equipes_apoio/<int:id>', methods=['GET'])
def get_equipe_apoio(id):
    equipe = EquipeApoio.query.get_or_404(id)
    return jsonify(equipe.serialize())

@bp.route('/equipes_apoio/<int:id>', methods=['PUT'])
def update_equipe_apoio(id):
    equipe = EquipeApoio.query.get_or_404(id)
    data = request.json
    equipe.candidato_id = data['candidato_id']
    equipe.ano = data['ano']
    db.session.commit()
    return jsonify({'message': 'Equipe de apoio atualizada com sucesso!'})

@bp.route('/equipes_apoio/<int:id>', methods=['DELETE'])
def delete_equipe_apoio(id):
    equipe = EquipeApoio.query.get_or_404(id)
    db.session.delete(equipe)
    db.session.commit()
    return jsonify({'message': 'Equipe de apoio deletada com sucesso!'})


# CRUD for ParticipanteEquipe
@bp.route('/participantes_equipes', methods=['GET'])
def get_participantes_equipes():
    participantes = ParticipanteEquipe.query.all()
    return jsonify([participante.serialize() for participante in participantes])

@bp.route('/participantes_equipes', methods=['POST'])
def create_participante_equipe():
    data = request.json
    participante = ParticipanteEquipe(pessoa_id=data['pessoa_id'], equipe_apoio_id=data['equipe_apoio_id'])
    db.session.add(participante)
    db.session.commit()
    return jsonify({'message': 'Participante de equipe criado com sucesso!'}), 201

@bp.route('/participantes_equipes/<int:id>', methods=['GET'])
def get_participante_equipe(id):
    participante = ParticipanteEquipe.query.get_or_404(id)
    return jsonify(participante.serialize())

@bp.route('/participantes_equipes/<int:id>', methods=['PUT'])
def update_participante_equipe(id):
    participante = ParticipanteEquipe.query.get_or_404(id)
    data = request.json
    participante.pessoa_id = data['pessoa_id']
    participante.equipe_apoio_id = data['equipe_apoio_id']
    db.session.commit()
    return jsonify({'message': 'Participante de equipe atualizado com sucesso!'})

@bp.route('/participantes_equipes/<int:id>', methods=['DELETE'])
def delete_participante_equipe(id):
    participante = ParticipanteEquipe.query.get_or_404(id)
    db.session.delete(participante)
    db.session.commit()
    return jsonify({'message': 'Participante de equipe deletado com sucesso!'})


# CRUD for Doador
@bp.route('/doadores', methods=['GET'])
def get_doadores():
    doadores = Doador.query.all()
    return jsonify([doador.serialize() for doador in doadores])

@bp.route('/doadores', methods=['POST'])
def create_doador():
    data = request.json
    doador = Doador(nome=data['nome'], tipo=data['tipo'])
    db.session.add(doador)
    db.session.commit()
    return jsonify({'message': 'Doador criado com sucesso!'}), 201

@bp.route('/doadores/<int:id>', methods=['GET'])
def get_doador(id):
    doador = Doador.query.get_or_404(id)
    return jsonify(doador.serialize())

@bp.route('/doadores/<int:id>', methods=['PUT'])
def update_doador(id):
    doador = Doador.query.get_or_404(id)
    data = request.json
    doador.nome = data['nome']
    doador.tipo = data['tipo']
    db.session.commit()
    return jsonify({'message': 'Doador atualizado com sucesso!'})

@bp.route('/doadores/<int:id>', methods=['DELETE'])
def delete_doador(id):
    doador = Doador.query.get_or_404(id)
    db.session.delete(doador)
    db.session.commit()
    return jsonify({'message': 'Doador deletado com sucesso!'})


# CRUD for Doacao
@bp.route('/doacoes', methods=['GET'])
def get_doacoes():
    doacoes = Doacao.query.all()
    return jsonify([doacao.serialize() for doacao in doacoes])

@bp.route('/doacoes', methods=['POST'])
def create_doacao():
    data = request.json
    doacao = Doacao(doador_id=data['doador_id'], candidato_id=data['candidato_id'], valor=data['valor'], data=data['data'])
    db.session.add(doacao)
    db.session.commit()
    return jsonify({'message': 'Doação criada com sucesso!'}), 201

@bp.route('/doacoes/<int:id>', methods=['GET'])
def get_doacao(id):
    doacao = Doacao.query.get_or_404(id)
    return jsonify(doacao.serialize())

@bp.route('/doacoes/<int:id>', methods=['PUT'])
def update_doacao(id):
    doacao = Doacao.query.get_or_404(id)
    data = request.json
    doacao.doador_id = data['doador_id']
    doacao.candidato_id = data['candidato_id']
    doacao.valor = data['valor']
    doacao.data = data['data']
    db.session.commit()
    return jsonify({'message': 'Doação atualizada com sucesso!'})

@bp.route('/doacoes/<int:id>', methods=['DELETE'])
def delete_doacao(id):
    doacao = Doacao.query.get_or_404(id)
    db.session.delete(doacao)
    db.session.commit()
    return jsonify({'message': 'Doação deletada com sucesso!'})


# CRUD for Pleito
@bp.route('/pleitos', methods=['GET'])
def get_pleitos():
    pleitos = Pleito.query.all()
    return jsonify([pleito.serialize() for pleito in pleitos])

@bp.route('/pleitos', methods=['POST'])
def create_pleito():
    data = request.json
    pleito = Pleito(ano=data['ano'], cargo_id=data['cargo_id'], candidato_id=data['candidato_id'], votos_recebidos=data['votos_recebidos'])
    db.session.add(pleito)
    db.session.commit()
    return jsonify({'message': 'Pleito criado com sucesso!'}), 201

@bp.route('/pleitos/<int:id>', methods=['GET'])
def get_pleito(id):
    pleito = Pleito.query.get_or_404(id)
    return jsonify(pleito.serialize())

@bp.route('/pleitos/<int:id>', methods=['PUT'])
def update_pleito(id):
    pleito = Pleito.query.get_or_404(id)
    data = request.json
    pleito.ano = data['ano']
    pleito.cargo_id = data['cargo_id']
    pleito.candidato_id = data['candidato_id']
    pleito.votos_recebidos = data['votos_recebidos']
    db.session.commit()
    return jsonify({'message': 'Pleito atualizado com sucesso!'})

@bp.route('/pleitos/<int:id>', methods=['DELETE'])
def delete_pleito(id):
    pleito = Pleito.query.get_or_404(id)
    db.session.delete(pleito)
    db.session.commit()
    return jsonify({'message': 'Pleito deletado com sucesso!'})
