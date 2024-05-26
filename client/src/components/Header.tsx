import { Component } from "solid-js";

export const Header: Component = () => {
  return (
    <div class="navbar bg-base-200 p-4">
      <div class="flex-1">
        <a class="btn btn-ghost text-xl">electoral-system</a>
      </div>
      <div class="flex-none gap-2">
        <div class="form-control">
          <input
            type="text"
            placeholder="Search"
            class="input input-bordered w-24 md:w-auto"
          />
        </div>
      </div>
    </div>
  );
};
