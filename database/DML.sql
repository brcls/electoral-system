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

INSERT INTO partido (nome, programa) VALUES 
('Partido Trabalhista', 'Nosso compromisso é com a justiça social e a igualdade.'),
('Partido Liberal', 'Promovemos a liberdade econômica e o empreendedorismo.'),
('Partido Verde', 'Defendemos a sustentabilidade e a preservação ambiental.'),
('Partido Conservador', 'Valorizamos os valores tradicionais e a segurança pública.');

INSERT INTO cargo (nome, tipo, local, quantidade_eleitos) VALUES 
('Presidente', 'Federal', 'Brasil', 1),
('Governador', 'Estadual', 'São Paulo', 1),
('Prefeito', 'Municipal', 'São Paulo', 1),
('Deputado Federal', 'Federal', 'Brasil', 513),
('Deputado Estadual', 'Estadual', 'São Paulo', 94),
('Vereador', 'Municipal', 'São Paulo', 55);

INSERT INTO pessoa (nome, data_nascimento) VALUES 
('João Silva', '1970-04-12'),
('Ana Costa', '1982-08-21'),
('Pedro Almeida', '1978-01-30'),
('Mariana Rocha', '1990-11-05'),
('Carlos Souza', '1965-09-23'),
('Fernanda Ramos', '1985-06-15'),
('Lucas Pereira', '1975-07-30'),
('Paula Mendes', '1992-10-18');

INSERT INTO candidato (pessoa_id, partido_id, cargo_id, data_candidatura, vice_candidato_id) VALUES 
(1, 1, 1, '2024-05-01', 1), -- João Silva para Presidente com Ana Costa como vice
(3, 2, 2, '2024-05-01', 2), -- Pedro Almeida para Governador de SP
(4, 3, 3, '2024-05-01', 3), -- Mariana Rocha para Prefeita de SP
(5, 4, 4, '2024-05-01', 4), -- Carlos Souza para Deputado Federal
(6, 1, 5, '2024-05-01', NULL), -- Fernanda Ramos para Deputada Estadual de SP
(7, 3, 6, '2024-05-01', NULL); -- Lucas Pereira para Vereador de SP

INSERT INTO processo_judicial (candidato_id, status, resultado, data_inicio, data_termino) VALUES 
(1, 'Em Tramitação', 'Procedente', '2023-01-15', NULL),
(2, 'Julgado', 'Não Procedente', '2021-03-10', '2022-02-20'),
(3, 'Em Tramitação', 'Não Procedente', '2022-06-05', NULL),
(4, 'Julgado', 'Procedente', '2019-08-30', '2020-07-15'),
(5, 'Em Tramitação', 'Procedente', '2022-09-01', NULL);

INSERT INTO equipe_apoio (candidato_id, ano) VALUES 
(1, 2024),
(3, 2024),
(4, 2024),
(5, 2024),
(6, 2024);

INSERT INTO participante_equipe (pessoa_id, equipe_apoio_id) VALUES 
(2, 1), -- Ana Costa na equipe de apoio de João Silva
(3, 3), -- Pedro Almeida na equipe de apoio de si mesmo
(4, 4), -- Mariana Rocha na equipe de apoio de si mesma
(5, 5), -- Carlos Souza na equipe de apoio de si mesmo
(6, 5); -- Fernanda Ramos na equipe de apoio de si mesma

INSERT INTO doador (nome, tipo) VALUES 
('Companhia ABC', 'Empresa'),
('Maria Ferreira', 'Indivíduo'),
('João Pereira', 'Indivíduo');

INSERT INTO doacao (doador_id, candidato_id, valor, data) VALUES 
(1, 1, 150000.00, '2024-04-10'), -- Companhia ABC doa para João Silva
(2, 3, 10000.00, '2024-04-15'), -- Maria Ferreira doa para Pedro Almeida
(3, 4, 5000.00, '2024-04-20'); -- João Pereira doa para Mariana Rocha

INSERT INTO pleito (ano, cargo_id, candidato_id, votos_recebidos) VALUES 
(2024, 1, 1, 60000000), -- João Silva concorre a Presidente em 2024
(2024, 2, 3, 15000000), -- Pedro Almeida concorre a Governador de SP em 2024
(2024, 3, 4, 8000000), -- Mariana Rocha concorre a Prefeita de SP em 2024
(2024, 4, 5, 3000000), -- Carlos Souza concorre a Deputado Federal em 2024
(2024, 5, 6, 5000000); -- Lucas Pereira concorre a Vereador de SP em 2024
