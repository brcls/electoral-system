import {
  Show,
  createEffect,
  createResource,
  createSignal,
  onMount,
  type Component,
} from "solid-js";
import { Header } from "./components/Header";

async function fetchCandidatos(): Promise<Candidatura[]> {
  const response = await fetch("http://127.0.0.1:5000/candidatos");
  if (!response.ok) {
    throw new Error("Erro ao buscar dados");
  }
  const data = await response.json();
  return data;
}

async function fetchPartidos(): Promise<Partido[]> {
  const response = await fetch("http://127.0.0.1:5000/partidos");
  if (!response.ok) {
    throw new Error("Erro ao buscar dados");
  }
  const data = await response.json();
  return data;
}

async function fetchCargos(): Promise<Cargo[]> {
  const response = await fetch("http://127.0.0.1:5000/cargos");
  if (!response.ok) {
    throw new Error("Erro ao buscar dados");
  }
  const data = await response.json();
  return data;
}

interface FiltroCandidato {
  ficha?: string; // Resultado do processo judicial
  cargo?: string; // Cargo do candidato
  partido?: string; // Partido do candidato
  data?: string; // Ano de candidatura
  temVice?: string;
}

const App: Component = () => {
  const [candidatos, setCandidatos] = createSignal([]);
  const [candidatosFiltrados, setcandidatosFiltrados] = createSignal([]);
  const [partidos, setPartidos] = createSignal([]);
  const [cargos, setCargos] = createSignal([]);
  const [datas, setDatas] = createSignal([]);
  const [nomes, setNomes] = createSignal([]);
  const [filtro, setFiltro] = createSignal(null);
  const [searchTerm, setSearchTerm] = createSignal("");

  onMount(() => {
    fetchCandidatos().then((data) => {
      setCandidatos(data);
      const dataMap = new Set(
        data.map((item) => new Date(item.data_candidatura).getFullYear()),
      );
      setDatas(Array.from(dataMap));
      const nomeMap = new Set(data.map((item) => item.pessoa.nome));
      setNomes(Array.from(nomeMap));
    });
    fetchPartidos().then(setPartidos);
    fetchCargos().then(setCargos);
  });

  createEffect(
    () => setcandidatosFiltrados(filtrarCandidatos(candidatos(), filtro())),
    [filtro],
  );

  createEffect(
    () => setcandidatosFiltrados(filtrarPorBusca(candidatos(), searchTerm())),
    [searchTerm],
  );

  const filtrarPorBusca = (candidatos: Candidatura[], filtro: string) => {
    return candidatos.filter((item) =>
      item.pessoa.nome.toLowerCase().includes(filtro.toLowerCase()),
    );
  };

  async function deleteCandidato(id: number): Promise<void> {
    try {
      const response = await fetch(`http://127.0.0.1:5000/candidatos/${id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Erro ao excluir dados");
      }

      setCandidatos((prevCandidatos) =>
        prevCandidatos.filter((candidato) => candidato.id !== id),
      );
    } catch (error) {
      console.error("Erro:", error.message);
    }
  }

  function filtrarCandidatos(
    candidatos: Candidatura[],
    filtro: FiltroCandidato | null,
  ) {
    return candidatos.filter((candidato) => {
      // Verificar se a candidatura é procedente ou não procedente
      const processoFiltrado =
        !filtro ||
        !filtro.ficha ||
        candidato.processos_judiciais.some(
          (processo) => processo.resultado === filtro.ficha,
        );

      // Filtrar por cargo
      const cargoFiltrado =
        !filtro || !filtro.cargo || candidato.cargo.nome === filtro.cargo;

      // Filtrar por partido
      const partidoFiltrado =
        !filtro || !filtro.partido || candidato.partido.nome === filtro.partido;

      // Filtrar por ano de candidatura
      const anoFiltrado =
        !filtro ||
        !filtro.data ||
        new Date(candidato.data_candidatura).getFullYear() ===
          parseInt(filtro.data);

      const viceFiltrado =
        !filtro ||
        !filtro.temVice ||
        (filtro.temVice === "sim" && candidato.vice_candidato) ||
        (filtro.temVice === "nao" && !candidato.vice_candidato);

      // Retornar true se todos os critérios forem atendidos
      return (
        processoFiltrado &&
        cargoFiltrado &&
        partidoFiltrado &&
        anoFiltrado &&
        viceFiltrado
      );
    });
  }

  return (
    <>
      <Header />
      <div class="my-10 flex w-full flex-col items-center gap-4">
        <Show when={candidatos()} fallback={<p>Carregando...</p>}>
          {(data) => {
            console.log(data());

            return (
              <>
                <div class="flex w-11/12 flex-wrap items-center justify-between gap-4">
                  <input
                    type="text"
                    placeholder="Procure pelo nome do candidato"
                    class="input input-bordered w-full"
                    value={searchTerm()}
                    onInput={(e) => setSearchTerm(e.target.value)}
                  />
                  <select
                    class="select select-bordered w-[49%]"
                    onChange={(e) =>
                      setFiltro({ ...filtro(), ficha: e.target.value })
                    }
                    value={filtro()?.ficha ?? ""}
                  >
                    <option value="">Ficha</option>
                    <option value="Procedente">Procedente</option>
                    <option value="Não Procedente">Não Procedente</option>
                  </select>
                  <select
                    class="select select-bordered w-[49%]"
                    onChange={(e) =>
                      setFiltro({ ...filtro(), cargo: e.target.value })
                    }
                    value={filtro()?.cargo ?? ""}
                  >
                    <option value="">Cargo</option>
                    {cargos().map((item) => (
                      <option value={item.nome}>{item.nome}</option>
                    ))}
                  </select>
                  <select
                    class="select select-bordered w-[49%]"
                    onChange={(e) =>
                      setFiltro({ ...filtro(), partido: e.target.value })
                    }
                    value={filtro()?.partido ?? ""}
                  >
                    <option value="">Partido</option>
                    {partidos().map((item) => (
                      <option value={item.nome}>{item.nome}</option>
                    ))}
                  </select>
                  <select
                    class="select select-bordered w-[49%]"
                    onChange={(e) =>
                      setFiltro({ ...filtro(), data: e.target.value })
                    }
                    value={filtro()?.data ?? ""}
                  >
                    <option value="">Ano de candidatura</option>
                    {datas().map((item) => (
                      <option value={item}>{item}</option>
                    ))}
                  </select>

                  <select
                    class="select select-bordered w-[49%]"
                    onChange={(e) =>
                      setFiltro({ ...filtro(), temVice: e.target.value })
                    }
                    value={filtro()?.temVice ?? ""}
                  >
                    <option value="">Tem Vice</option>
                    <option value="sim">Sim</option>
                    <option value="nao">Não</option>
                  </select>
                  <button
                    class="btn btn-neutral w-[49%]"
                    onClick={() => setFiltro(null)}
                  >
                    Limpar filtro
                  </button>
                </div>
                {candidatosFiltrados()?.length &&
                  candidatosFiltrados().map((item) => (
                    <div class="w-11/12 rounded-xl bg-base-200 p-7">
                      <div class="flex items-center justify-between">
                        <p class="text-2xl hover:cursor-pointer hover:underline">
                          {item.pessoa.nome}
                        </p>
                        <p class="text-lg">{item.cargo.nome}</p>
                        <p class="text-lg">{item.partido.nome}</p>
                        <p class="text-lg">{item.data_candidatura}</p>
                        <p
                          class="text-lg text-red-500 hover:cursor-pointer hover:underline"
                          onClick={async () => await deleteCandidato(item.id)}
                        >
                          deletar
                        </p>
                      </div>
                      <div class="divider"></div>
                      <div class="flex justify-between gap-4">
                        {item.participantes_equipe?.length && (
                          <div class="w-full flex-col gap-4 rounded-xl bg-base-300 px-4 py-6">
                            <p class="text-lg">Equipe de apoio</p>
                            <div class="divider"></div>
                            {item.participantes_equipe.map((pessoa) => (
                              <div class="hover:cursor-pointer hover:underline">
                                {pessoa.nome}
                              </div>
                            ))}
                          </div>
                        )}

                        {item.processos_judiciais?.length && (
                          <div class="w-full gap-4 rounded-xl bg-base-300 p-6">
                            <p class="text-lg">Processos Judiciais</p>
                            <div class="divider"></div>
                            {item.processos_judiciais.map((processo) => (
                              <div class="hover:cursor-pointer hover:underline">
                                {processo.data_inicio} - {processo.status} -{" "}
                                {processo.resultado}
                              </div>
                            ))}
                          </div>
                        )}
                        {item.doacoes?.length && (
                          <div class="w-full gap-4 rounded-xl bg-base-300 px-4 py-6">
                            <p class="text-lg">Doações</p>
                            <div class="divider"></div>
                            {item.doacoes.map((doacao) => (
                              <div class="hover:cursor-pointer hover:underline">
                                R$ {doacao.valor}
                              </div>
                            ))}
                          </div>
                        )}
                        {item.vice_candidato !== null && (
                          <div class="w-full gap-4 rounded-xl bg-base-300 px-4 py-6">
                            <p class="text-lg">Vice Candidato</p>
                            <div class="divider"></div>
                            <div class="hover:cursor-pointer hover:underline">
                              {item.vice_candidato.nome}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
              </>
            );
          }}
        </Show>
      </div>
    </>
  );
};

export default App;
