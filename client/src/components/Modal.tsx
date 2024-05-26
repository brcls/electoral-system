import { Component } from "solid-js";

export const Modal: Component = () => {
  return (
    <dialog id="my_modal_1" class="modal">
      <div class="modal-box w-11/12 max-w-5xl">
        <h3 class="text-lg font-bold">Hello!</h3>
        <p class="py-4">Click the button below to close</p>
        <div class="modal-action">
          <form method="dialog">
            <button class="btn">Close</button>
          </form>
        </div>
      </div>
      <form method="dialog" class="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
  );
};
