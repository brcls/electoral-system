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

-- Adicionando mais registros às tabelas

-- Adicionando mais partidos
INSERT INTO partido (nome, programa) VALUES 
('Partido Socialista', 'Lutamos pela justiça social e redistribuição de riqueza.'),
('Partido Progressista', 'Foco na inovação tecnológica e educação.'),
('Partido Democrático', 'Fortalecemos a democracia e os direitos humanos.'),
('Partido Nacionalista', 'Valorizamos a identidade nacional e a soberania.'),
('Partido Liberal Democrático', 'Defendemos as liberdades individuais e a economia de mercado.'),
('Partido Comunista', 'Revolução proletária e abolição da propriedade privada.'),
('Partido Social Democrata', 'Busca de um equilíbrio entre mercado e bem-estar social.'),
('Partido Republicano', 'Valores conservadores e direitos individuais.'),
('Partido Trabalhista Cristão', 'Combina justiça social com princípios cristãos.'),
('Partido Ecologista', 'Prioridade à preservação ambiental e sustentabilidade.');

-- Adicionando mais cargos
INSERT INTO cargo (nome, tipo, local, quantidade_eleitos) VALUES 
('Senador', 'Federal', 'Brasil', 81),
('Deputado Distrital', 'Distrital', 'Distrito Federal', 24),
('Vereador', 'Municipal', 'Rio de Janeiro', 51),
('Prefeito', 'Municipal', 'Rio de Janeiro', 1),
('Governador', 'Estadual', 'Minas Gerais', 1),
('Deputado Estadual', 'Estadual', 'Minas Gerais', 77),
('Senador', 'Federal', 'São Paulo', 3),
('Vereador', 'Municipal', 'Belo Horizonte', 41),
('Prefeito', 'Municipal', 'Belo Horizonte', 1),
('Deputado Estadual', 'Estadual', 'Rio de Janeiro', 70);

-- Adicionando mais pessoas
INSERT INTO pessoa (nome, data_nascimento) VALUES 
('Juliana Martins', '1980-12-14'),
('Rafael Nunes', '1975-03-23'),
('Beatriz Oliveira', '1988-07-19'),
('Roberto Lima', '1993-05-09'),
('Sofia Carvalho', '1972-10-25'),
('Gustavo Ferreira', '1983-02-11'),
('Clara Mendes', '1987-09-13'),
('Eduardo Franco', '1991-04-04'),
('Isabela Almeida', '1978-11-22'),
('Marcelo Pereira', '1969-05-18'),
('Fernanda Souza', '1990-06-07'),
('Tiago Silva', '1982-03-30'),
('Camila Ramos', '1975-01-17'),
('Rodrigo Costa', '1989-08-25'),
('Larissa Rodrigues', '1994-12-09'),
('Gabriel Santos', '1985-02-12'),
('Bruna Fernandes', '1977-03-05'),
('Felipe Barros', '1984-10-10'),
('Renata Machado', '1986-11-03'),
('Fernando Castro', '1973-02-19'),
('Ana Silva', '1990-03-15'),
('Pedro Santos', '1985-07-20'),
('Mariana Oliveira', '1992-11-10'),
('Lucas Pereira', '1988-05-03'),
('Juliana Martins', '1987-09-18'),
('Rafael Nunes', '1991-02-25'),
('Beatriz Oliveira', '1989-12-08'),
('Roberto Lima', '1986-06-30'),
('Sofia Carvalho', '1993-04-22'),
('Gustavo Ferreira', '1984-08-12'),
('Clara Mendes', '1990-10-05'),
('Eduardo Franco', '1989-01-28'),
('Isabela Almeida', '1995-06-15'),
('Marcelo Pereira', '1987-09-20'),
('Fernanda Souza', '1991-03-11'),
('Tiago Silva', '1988-07-02'),
('Camila Ramos', '1992-11-18'),
('Rodrigo Costa', '1986-12-30'),
('Larissa Rodrigues', '1994-04-25'),
('Gabriel Santos', '1985-08-17');

-- Adicionando mais candidatos
INSERT INTO candidato (pessoa_id, partido_id, cargo_id, data_candidatura, vice_candidato_id) VALUES 
(1, 1, 2, '2024-05-01', NULL), -- Rafael Nunes para Deputado Distrital
(2, 3, 3, '2024-05-01', NULL), -- Beatriz Oliveira para Vereadora do RJ
(3, 5, 5, '2024-05-01', NULL), -- Sofia Carvalho para Senadora
(4, 6, 6, '2024-05-01', NULL), -- Gustavo Ferreira para Vereador do RJ
(5, 8, 8, '2024-05-01', NULL), -- Eduardo Franco para Vereador em BH
(6, 9, 9, '2024-05-01', NULL), -- Isabela Almeida para Prefeita de BH
(7, 2, 3, '2024-05-01', NULL), -- Tiago Silva para Vereador do RJ
(8, 3, 2, '2024-05-01', NULL), -- Camila Ramos para Deputada Distrital
(9, 4, 1, '2024-05-01', NULL), -- Rodrigo Costa para Presidente
(10, 5, 8, '2024-05-01', NULL), -- Larissa Rodrigues para Vereadora em BH
(11, 6, 7, '2024-05-01', NULL), -- Gabriel Santos para Senador por SP
(12, 7, 6, '2024-05-01', NULL), -- Bruna Fernandes para Deputada Estadual no RJ
(13, 8, 5, '2024-05-01', NULL), -- Felipe Barros para Senador por MG
(14, 9, 4, '2024-05-01', NULL), -- Renata Machado para Prefeita do RJ
(15, 10, 3, '2024-05-01', NULL)

INSERT INTO candidato (pessoa_id, partido_id, cargo_id, data_candidatura, vice_candidato_id) VALUES 
(16, 2, 1, '2024-05-01', 2), -- Juliana Martins para Senadora com Rafael Nunes como vice
(17, 4, 4, '2024-05-01', 3), -- Roberto Lima para Prefeito do RJ com Beatriz Oliveira como vice
(18, 7, 7, '2024-05-01', 5), -- Clara Mendes para Senadora com Sofia Carvalho como vice
(19, 10, 10, '2024-05-01', 6), -- Marcelo Pereira para Deputado Estadual no RJ com Gustavo Ferreira como vice
(20, 1, 4, '2024-05-01', 4); -- Fernanda Souza para Prefeita do RJ com Beatriz Oliveira como vice

-- Adicionando mais processos judiciais
INSERT INTO processo_judicial (candidato_id, status, resultado, data_inicio, data_termino) VALUES 
(6, 'Julgado', 'Não Procedente', '2020-02-01', '2021-01-10'),
(7, 'Em Tramitação', 'Procedente', '2023-03-15', NULL),
(8, 'Julgado', 'Procedente', '2022-11-20', '2023-04-30'),
(9, 'Em Tramitação', 'Não Procedente', '2021-07-22', NULL),
(10, 'Julgado', 'Procedente', '2020-05-17', '2021-06-28'),
(11, 'Em Tramitação', 'Procedente', '2023-01-01', NULL),
(12, 'Julgado', 'Não Procedente', '2022-04-12', '2022-12-01'),
(13, 'Em Tramitação', 'Procedente', '2023-05-10', NULL),
(14, 'Julgado', 'Procedente', '2021-08-15', '2022-03-20'),
(15, 'Em Tramitação', 'Não Procedente', '2022-10-20', NULL),
(16, 'Julgado', 'Procedente', '2019-09-25', '2020-07-15'),
(17, 'Em Tramitação', 'Procedente', '2021-11-11', NULL),
(18, 'Julgado', 'Não Procedente', '2020-02-20', '2020-12-20'),
(19, 'Em Tramitação', 'Procedente', '2023-03-30', NULL),
(20, 'Julgado', 'Procedente', '2021-07-10', '2022-05-25');

-- Adicionando mais equipes de apoio
INSERT INTO equipe_apoio (candidato_id, ano) VALUES 
(1, 2021),
(2, 2022),
(3, 2023),
(4, 2024),
(5, 2021),
(6, 2022),
(7, 2023),
(8, 2024),
(9, 2021),
(10, 2022),
(11, 2023),
(12, 2024),
(13, 2021),
(14, 2022),
(15, 2023),
(16, 2024),
(17, 2021),
(18, 2022),
(19, 2023),
(20, 2024);

-- Adicionando mais participantes de equipe
INSERT INTO participante_equipe (pessoa_id, equipe_apoio_id) VALUES 
(1, 1), -- Lucas Pereira na equipe 1
(21, 1), -- Ana Silva na equipe 1
(2, 2), -- Juliana Martins na equipe 2
(22, 2), -- Pedro Santos na equipe 2
(3, 3), -- Rafael Nunes na equipe 3
(23, 3), -- Mariana Oliveira na equipe 3
(4, 4), -- Beatriz Oliveira na equipe 4
(24, 4), -- Lucas Pereira na equipe 4
(5, 5), -- Roberto Lima na equipe 5
(25, 5), -- Juliana Martins na equipe 5
(6, 6), -- Sofia Carvalho na equipe 6
(26, 6), -- Rafael Nunes na equipe 6
(7, 7), -- Gustavo Ferreira na equipe 7
(27, 7), -- Beatriz Oliveira na equipe 7
(8, 8), -- Clara Mendes na equipe 8
(28, 8), -- Sofia Carvalho na equipe 8
(9, 9), -- Eduardo Franco na equipe 9
(29, 9), -- Gustavo Ferreira na equipe 9
(10, 10), -- Isabela Almeida na equipe 10
(30, 10), -- Clara Mendes na equipe 10
(11, 11), -- Marcelo Pereira na equipe 11
(31, 11), -- Eduardo Franco na equipe 11
(12, 12), -- Fernanda Souza na equipe 12
(32, 12), -- Isabela Almeida na equipe 12
(13, 13), -- Tiago Silva na equipe 13
(33, 13), -- Marcelo Pereira na equipe 13
(14, 14), -- Camila Ramos na equipe 14
(34, 14), -- Fernanda Souza na equipe 14
(15, 15), -- Rodrigo Costa na equipe 15
(35, 15), -- Tiago Silva na equipe 15
(16, 16), -- Larissa Rodrigues na equipe 16
(36, 16), -- Camila Ramos na equipe 16
(17, 17), -- Gabriel Santos na equipe 17
(37, 17), -- Rodrigo Costa na equipe 17
(18, 18), -- Bruna Fernandes na equipe 18
(38, 18), -- Larissa Rodrigues na equipe 18
(19, 19), -- Felipe Barros na equipe 19
(39, 19), -- Gabriel Santos na equipe 19
(20, 20), -- Renata Machado na equipe 20
(40, 20); -- Bruna Fernandes na equipe 20

-- Adicionando mais doadores
INSERT INTO doador (nome, tipo) VALUES 
('Empresa XYZ', 'Empresa'),
('Felipe Andrade', 'Indivíduo'),
('Carla Mello', 'Indivíduo'),
('José Santos', 'Indivíduo'),
('Ana Lima', 'Indivíduo'),
('Companhia ABC', 'Empresa'),
('Marta Souza', 'Indivíduo'),
('Lucas Gomes', 'Indivíduo'),
('Rosa Silva', 'Indivíduo'),
('Empresa Delta', 'Empresa'),
('Empresa E', 'Empresa'),
('Fernanda Oliveira', 'Indivíduo'),
('Carlos Silva', 'Indivíduo'),
('Paula Mendes', 'Indivíduo'),
('João Santos', 'Indivíduo'),
('Companhia FG', 'Empresa'),
('Mariana Costa', 'Indivíduo'),
('Pedro Alves', 'Indivíduo'),
('Roberta Santos', 'Indivíduo'),
('Empresa HIJ', 'Empresa');

-- Adicionando mais doações
INSERT INTO doacao (doador_id, candidato_id, valor, data) VALUES 
(1, 1, 200000.00, '2024-04-11'), -- Empresa XYZ doa para Pedro Almeida
(2, 2, 15000.00, '2024-04-18'), -- Felipe Andrade doa para Mariana Rocha
(3, 3, 7000.00, '2024-04-22'), -- Carla Mello doa para Carlos Souza
(4, 4, 50000.00, '2024-04-25'), -- Empresa XYZ doa para Fernanda Ramos
(5, 5, 8000.00, '2024-04-28'), -- Felipe Andrade doa para Lucas Pereira
(6, 6, 30000.00, '2024-05-02'), -- José Santos doa para Juliana Martins
(7, 7, 10000.00, '2024-05-05'), -- Ana Lima doa para Rafael Nunes
(8, 8, 5000.00, '2024-05-08'), -- Companhia ABC doa para Beatriz Oliveira
(9, 9, 20000.00, '2024-05-11'), -- Marta Souza doa para Roberto Lima
(10, 10, 12000.00, '2024-05-14'), -- Lucas Gomes doa para Sofia Carvalho
(11, 11, 60000.00, '2024-05-17'), -- Rosa Silva doa para Gustavo Ferreira
(12, 12, 15000.00, '2024-05-20'), -- Empresa Delta doa para Clara Mendes
(13, 13, 5000.00, '2024-05-23'), -- Empresa XYZ doa para Eduardo Franco
(14, 14, 3000.00, '2024-05-26'), -- Felipe Andrade doa para Isabela Almeida
(15, 15, 8000.00, '2024-05-29'), -- Carla Mello doa para Marcelo Pereira
(16, 16, 25000.00, '2024-06-01'), -- José Santos doa para Fernanda Souza
(17, 17, 15000.00, '2024-06-04'), -- Ana Lima doa para Tiago Silva
(18, 18, 9000.00, '2024-06-07'), -- Companhia ABC doa para Camila Ramos
(19, 19, 30000.00, '2024-06-10'), -- Marta Souza doa para Rodrigo Costa
(20, 20, 12000.00, '2024-06-13'); -- Lucas Gomes doa para Larissa Rodrigues

-- Adicionando mais pleitos
INSERT INTO pleito (ano, cargo_id, candidato_id, votos_recebidos) VALUES 
(2024, 6, 7, 4000000), -- Lucas Pereira concorre a Vereador no RJ em 2024
(2024, 7, 8, 3000000), -- Juliana Martins concorre a Senadora em 2024
(2024, 8, 9, 2500000), -- Rafael Nunes concorre a Deputado Distrital em 2024
(2024, 9, 10, 500000), -- Beatriz Oliveira concorre a Vereadora no RJ em 2024
(2024, 10, 11, 3500000), -- Roberto Lima concorre a Prefeito no RJ em 2024
(2024, 1, 12, 1000000), -- Sofia Carvalho concorre a Senadora em 2024
(2024, 2, 13, 700000), -- Gustavo Ferreira concorre a Vereador no RJ em 2024
(2024, 3, 14, 600000), -- Clara Mendes concorre a Senadora em 2024
(2024, 4, 15, 800000), -- Eduardo Franco concorre a Vereador em BH em 2024
(2024, 5, 16, 500000), -- Isabela Almeida concorre a Prefeita de BH em 2024
(2024, 6, 17, 400000), -- Marcelo Pereira concorre a Deputado Estadual no RJ em 2024
(2024, 7, 18, 700000), -- Fernanda Souza concorre a Prefeita do RJ em 2024
(2024, 8, 19, 600000), -- Tiago Silva concorre a Vereador do RJ em 2024
(2024, 9, 20, 500000); -- Camila Ramos concorre a Deputada Distrital em 2024

-- Redefinindo a sequência para a tabela partido
ALTER SEQUENCE partido_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela cargo
ALTER SEQUENCE cargo_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela pessoa
ALTER SEQUENCE pessoa_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela candidato
ALTER SEQUENCE candidato_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela processo_judicial
ALTER SEQUENCE processo_judicial_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela equipe_apoio
ALTER SEQUENCE equipe_apoio_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela participante_equipe
ALTER SEQUENCE participante_equipe_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela doador
ALTER SEQUENCE doador_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela doacao
ALTER SEQUENCE doacao_id_seq RESTART WITH 1;

-- Redefinindo a sequência para a tabela pleito
ALTER SEQUENCE pleito_id_seq RESTART WITH 1;

-- Esvaziar a tabela doacao
DELETE FROM doacao;

-- Esvaziar a tabela processo_judicial
DELETE FROM processo_judicial;

-- Esvaziar a tabela participante_equipe
DELETE FROM participante_equipe;

-- Esvaziar a tabela equipe_apoio
DELETE FROM equipe_apoio;

-- Esvaziar a tabela pleito
DELETE FROM pleito;

-- Esvaziar a tabela candidato
DELETE FROM candidato;

-- Esvaziar a tabela doador
DELETE FROM doador;

-- Esvaziar a tabela pessoa
DELETE FROM pessoa;

-- Esvaziar a tabela partido
DELETE FROM partido;

-- Esvaziar a tabela cargo
DELETE FROM cargo;
