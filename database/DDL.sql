-- Database: electoralsystem

-- DROP DATABASE IF EXISTS electoralsystem;

CREATE DATABASE electoralsystem
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Criação da tabela Partido
CREATE TABLE Partido (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Programa TEXT NOT NULL
);

-- Criação da tabela Cargo
CREATE TABLE Cargo (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Local VARCHAR(100) NOT NULL,
    QuantidadeEleitos INT NOT NULL
);

-- Criação da tabela Pessoa
CREATE TABLE Pessoa (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataNascimento DATE NOT NULL
);

-- Criação da tabela Candidato
CREATE TABLE Candidato (
    ID SERIAL PRIMARY KEY,
    PessoaID INT NOT NULL REFERENCES Pessoa(ID),
    PartidoID INT NOT NULL REFERENCES Partido(ID),
    CargoID INT NOT NULL REFERENCES Cargo(ID),
    DataCandidatura DATE NOT NULL,
    ViceCandidatoID INT REFERENCES Pessoa(ID)
);

-- Criação da tabela ProcessoJudicial
CREATE TABLE ProcessoJudicial (
    ID SERIAL PRIMARY KEY,
    CandidatoID INT NOT NULL REFERENCES Candidato(ID),
    Status VARCHAR(50) NOT NULL,
    Resultado VARCHAR(50),
    DataInicio DATE NOT NULL,
    DataTermino DATE
);

-- Criação da tabela EquipeApoio
CREATE TABLE EquipeApoio (
    ID SERIAL PRIMARY KEY,
    CandidatoID INT NOT NULL REFERENCES Candidato(ID),
    Ano INT NOT NULL
);

-- Criação da tabela ParticipanteEquipe
CREATE TABLE ParticipanteEquipe (
    ID SERIAL PRIMARY KEY,
    PessoaID INT NOT NULL REFERENCES Pessoa(ID),
    EquipeApoioID INT NOT NULL REFERENCES EquipeApoio(ID)
);

-- Criação da tabela Doador
CREATE TABLE Doador (
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50) NOT NULL
);

-- Criação da tabela Doacao
CREATE TABLE Doacao (
    ID SERIAL PRIMARY KEY,
    DoadorID INT NOT NULL REFERENCES Doador(ID),
    CandidatoID INT NOT NULL REFERENCES Candidato(ID),
    Valor DECIMAL(10, 2) NOT NULL,
    Data DATE NOT NULL
);

-- Criação da tabela Pleito
CREATE TABLE Pleito (
    ID SERIAL PRIMARY KEY,
    Ano INT NOT NULL,
    CargoID INT NOT NULL REFERENCES Cargo(ID),
    CandidatoID INT NOT NULL REFERENCES Candidato(ID),
    VotosRecebidos INT NOT NULL
);


-- Trigger para garantir que um candidato pode concorrer a apenas um cargo por ano
CREATE OR REPLACE FUNCTION check_unique_candidacy_per_year()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM Candidato 
        WHERE PessoaID = NEW.PessoaID 
        AND EXTRACT(YEAR FROM DataCandidatura) = EXTRACT(YEAR FROM NEW.DataCandidatura)
        AND ID != NEW.ID
    ) THEN
        RAISE EXCEPTION 'O candidato já está concorrendo a um cargo neste ano';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_unique_candidacy_per_year
BEFORE INSERT OR UPDATE ON Candidato
FOR EACH ROW
EXECUTE FUNCTION check_unique_candidacy_per_year();

-- Trigger para garantir que um indivíduo só pode participar de uma única equipe de apoio por ano
CREATE OR REPLACE FUNCTION check_unique_support_team_per_year()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM ParticipanteEquipe PE
        JOIN EquipeApoio EA ON PE.EquipeApoioID = EA.ID
        WHERE PE.PessoaID = NEW.PessoaID
        AND EA.Ano = (SELECT Ano FROM EquipeApoio WHERE ID = NEW.EquipeApoioID)
        AND PE.ID != NEW.ID
    ) THEN
        RAISE EXCEPTION 'O participante já está em uma equipe de apoio neste ano';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_unique_support_team_per_year
BEFORE INSERT OR UPDATE ON ParticipanteEquipe
FOR EACH ROW
EXECUTE FUNCTION check_unique_support_team_per_year();
