interface Doacao {
  candidato_id: number;
  data: string;
  doador_id: number;
  id: number;
  valor: string;
}

interface EquipeDeApoio {
  id: number;
  local: string;
  nome: string;
  quantidade_eleitos: number;
  tipo: string;
}

interface Partido {
  id: number;
  nome: string;
  programa: string;
}

interface Pessoa {
  data_nascimento: string;
  id: number;
  nome: string;
}

interface ProcessoJudicial {
  candidato_id: number;
  data_inicio: string;
  data_termino: string | null;
  id: number;
  resultado: string;
  status: string;
}

interface ViceCandidato {
  data_candidatura: string;
  id: number;
  partido_id: number;
}

interface Cargo {
  id: number;
  local: string;
  nome: string;
  quantidade_eleitos: number;
  tipo: string;
}

interface Candidatura {
  data_candidatura: string;
  doacoes: Doacao[];
  cargo: Cargo;
  equipe_de_apoio: EquipeDeApoio;
  id: number;
  partido: Partido;
  pessoa: Pessoa;
  processos_judiciais: ProcessoJudicial[];
  vice_candidato: ViceCandidato;
  participantes_equipe: Pessoa[];
}
