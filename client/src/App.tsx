import type { Component } from "solid-js";
import { Header } from "./components/Header";
import { Modal } from "./components/Modal";

const App: Component = () => {
  return (
    <>
      <Header />
      <Modal />
      <div class="my-10 flex w-screen flex-col items-center gap-4">
        <div class="flex w-11/12 items-center justify-between gap-4">
          <select class="select select-bordered w-full">
            <option disabled selected>
              Nome sujo
            </option>
            <option>Sim</option>
            <option>Não</option>
          </select>
          <select class="select select-bordered w-full">
            <option disabled selected>
              Cargo
            </option>
            <option>Han Solo</option>
            <option>Greedo</option>
          </select>
          <select class="select select-bordered w-full">
            <option disabled selected>
              Partido
            </option>
            <option>Han Solo</option>
            <option>Greedo</option>
          </select>
          <select class="select select-bordered w-full">
            <option disabled selected>
              Ano de candidatura
            </option>
            <option>Han Solo</option>
            <option>Greedo</option>
          </select>
        </div>
        {[0, 1, 2, 3, 4].map((item) => (
          <div class="w-11/12 rounded-xl bg-base-200 p-7">
            <div class="flex items-center justify-between">
              <p class="text-2xl">Candidato</p>
              <p class="text-lg">Cargo</p>
              <p class="text-lg">Partido</p>
              <p class="text-lg">2020 - 2024</p>
            </div>
            <div class="divider"></div>
            <div class="flex items-center justify-between gap-4">
              <div class="w-full gap-4 rounded-xl bg-base-300 p-4">
                <p class="text-lg">Equipe de apoio</p>
                <div class="divider"></div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Pessoa
                </div>

                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Pessoa
                </div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Pessoa
                </div>
                <p class="text-zinc-500 hover:cursor-pointer hover:underline">
                  ver mais...
                </p>
              </div>
              <div class="w-full gap-4 rounded-xl bg-base-300 p-4">
                <p class="text-lg">Processo Judiciais</p>
                <div class="divider"></div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Caso
                </div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Caso
                </div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Caso
                </div>
                <p class="text-zinc-500 hover:cursor-pointer hover:underline">
                  ver mais...
                </p>
              </div>
              <div class="w-full gap-4 rounded-xl bg-base-300 p-4">
                <p class="text-lg">Doadores</p>
                <div class="divider"></div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Instituição
                </div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Pessoa
                </div>
                <div
                  onClick={() =>
                    document.getElementById("my_modal_1").showModal()
                  }
                  class="hover:cursor-pointer hover:underline"
                >
                  Instituição
                </div>
                <p class="text-zinc-500 hover:cursor-pointer hover:underline">
                  ver mais...
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default App;
