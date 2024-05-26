# app/models.py

from . import db

class Partido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    programa = db.Column(db.Text, nullable=False)

class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    quantidade_eleitos = db.Column(db.Integer, nullable=False)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    data_candidatura = db.Column(db.Date, nullable=False)
    vice_candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=True)

class ProcessoJudicial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    resultado = db.Column(db.String(50), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_termino = db.Column(db.Date, nullable=True)

class EquipeApoio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

class ParticipanteEquipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    equipe_apoio_id = db.Column(db.Integer, db.ForeignKey('equipe_apoio.id'), nullable=False)

class Doador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doador_id = db.Column(db.Integer, db.ForeignKey('doador.id'), nullable=False)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data = db.Column(db.Date, nullable=False)

class Pleito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer, nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    votos_recebidos = db.Column(db.Integer, nullable=False)
