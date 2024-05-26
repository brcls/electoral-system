from . import db

class Partido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    programa = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'programa': self.programa
        }

class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    quantidade_eleitos = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'local': self.local,
            'quantidade_eleitos': self.quantidade_eleitos
        }

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d') if self.data_nascimento else None
        }

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    data_candidatura = db.Column(db.Date, nullable=False)
    vice_candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'pessoa_id': self.pessoa_id,
            'partido_id': self.partido_id,
            'cargo_id': self.cargo_id,
            'data_candidatura': self.data_candidatura.strftime('%Y-%m-%d') if self.data_candidatura else None,
            'vice_candidato_id': self.vice_candidato_id
        }

class ProcessoJudicial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    resultado = db.Column(db.String(50), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_termino = db.Column(db.Date, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'candidato_id': self.candidato_id,
            'status': self.status,
            'resultado': self.resultado,
            'data_inicio': self.data_inicio.strftime('%Y-%m-%d'),
            'data_termino': self.data_termino.strftime('%Y-%m-%d') if self.data_termino else None
        }

class EquipeApoio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'candidato_id': self.candidato_id,
            'ano': self.ano
        }

class ParticipanteEquipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    equipe_apoio_id = db.Column(db.Integer, db.ForeignKey('equipe_apoio.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'pessoa_id': self.pessoa_id,
            'equipe_apoio_id': self.equipe_apoio_id
        }

class Doador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo
        }

class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doador_id = db.Column(db.Integer, db.ForeignKey('doador.id'), nullable=False)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data = db.Column(db.Date, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'doador_id': self.doador_id,
            'candidato_id': self.candidato_id,
            'valor': str(self.valor),
            'data': self.data.strftime('%Y-%m-%d')
        }

class Pleito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer, nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    votos_recebidos = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'ano': self.ano,
            'cargo_id': self.cargo_id,
            'candidato_id': self.candidato_id,
            'votos_recebidos': self.votos_recebidos
        }
