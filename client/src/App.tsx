import { Show, createResource, createSignal, type Component } from "solid-js";
import { Header } from "./components/Header";
import { Modal } from "./components/Modal";

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

const App: Component = () => {
  const [candidatos, setCandidatos] = createSignal([]);
  fetchCandidatos().then(setCandidatos);

  const [partidos] = createResource<Partido[]>(fetchPartidos);
  const [cargos] = createResource<Cargo[]>(fetchCargos);

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

  return (
    <>
      <Header />
      <Modal />
      <div class="my-10 flex w-full flex-col items-center gap-4">
        <Show when={candidatos()} fallback={<p>Carregando...</p>}>
          {(data) => (
            <>
              <div class="flex w-11/12 items-center justify-between gap-4">
                <select class="select select-bordered w-full">
                  <option disabled selected>
                    Ficha
                  </option>
                  <option>Procedente</option>
                  <option>Não procedente</option>
                </select>
                <Show when={cargos()} fallback={<p>Carregando...</p>}>
                  {(data) => (
                    <select class="select select-bordered w-full">
                      <option disabled selected>
                        Cargo
                      </option>
                      {data().map((item) => (
                        <option>{item.nome}</option>
                      ))}
                    </select>
                  )}
                </Show>
                <Show when={partidos()} fallback={<p>Carregando...</p>}>
                  {(data) => (
                    <select class="select select-bordered w-full">
                      <option disabled selected>
                        Partido
                      </option>
                      {data().map((item) => (
                        <option>{item.nome}</option>
                      ))}
                    </select>
                  )}
                </Show>
                <select class="select select-bordered w-full">
                  <option disabled selected>
                    Ano de candidatura
                  </option>
                  <option>Han Solo</option>
                  <option>Greedo</option>
                </select>
              </div>
              {data().map((item) => (
                <div class="w-11/12 rounded-xl bg-base-200 p-7">
                  <div class="flex items-center justify-between">
                    <p
                      class="text-2xl hover:cursor-pointer hover:underline"
                      onClick={() =>
                        document.getElementById("my_modal_1").showModal()
                      }
                    >
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
                          <div
                            onClick={() =>
                              document.getElementById("my_modal_1").showModal()
                            }
                            class="hover:cursor-pointer hover:underline"
                          >
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
                          <div
                            onClick={() =>
                              document.getElementById("my_modal_1").showModal()
                            }
                            class="hover:cursor-pointer hover:underline"
                          >
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
                          <div
                            onClick={() =>
                              document.getElementById("my_modal_1").showModal()
                            }
                            class="hover:cursor-pointer hover:underline"
                          >
                            R$ {doacao.valor}
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </>
          )}
        </Show>
      </div>
    </>
  );
};

export default App;
