import { Component } from "solid-js";

export const Header: Component = () => {
  return (
    <div class="navbar bg-base-200 p-4">
      <div class="flex-1">
        <a class="btn btn-ghost text-xl">electoral-system</a>
      </div>
      {/* <div class="flex-none gap-2">
        <button class="btn btn-neutral">Adicionar Candidato</button>
      </div> */}
    </div>
  );
};
