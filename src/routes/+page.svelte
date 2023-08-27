<script>
    // Imports

    // Rust API
    import { invoke } from "@tauri-apps/api";
    import { listen } from "@tauri-apps/api/event";
    import { onMount, createEventDispatcher } from "svelte";
    import { writable } from "svelte/store";

    // Svelte Components
    import TicketButton from "$lib/TicketButton.svelte"
    import ReimageTable from "$lib/ReimageTable.svelte"
    import LoadingObject from "$lib/LoadingObject.svelte"

    // Images/Assets
    import eeficon from "$lib/assets/eeficon@2x.png"
    import cuiLogo from "$lib/assets/cui-logo@2x.png"

    // Variables
    let showLoading = true;

    // Example Function Call w/ Rust API
    // let name = "";
    // let output = "";
    // async function greet() {
    //     output = await invoke("greet", {name});
    // }


    const updateTickets = async () => {
      showLoading = true;
      let output = await invoke("update_tickets")
        .then((ticketArray) =>
        {
          tickets.set(ticketArray);
          showLoading = false;
        })
        .catch((err) => {
          console.log(err);
        });
      return output;
    }

    const cleanTicketUpdate = async () => {
      console.log("Clean Ticket Update");
      showLoading = true;
      let output = await invoke("clean_ticket_update")
        .then((ticketArray) =>
        {
          tickets.set(ticketArray);
          showLoading = false;
        })
        .catch((err) => {
          console.log(err);
        });
      return output;
    }


    export const tickets = writable([]);

    onMount(async () => {
      await cleanTicketUpdate();
    });

    const dispatch = createEventDispatcher();

    let reimagetableComp;

    function customListen(event){
      console.log("Button pressed");
      reimagetableComp.testListen();      
    }

    const listener = listen("backend-update-tickets", (event) => {
      console.log("Backend update tickets event received");
      cleanTicketUpdate();
    });


    function showGithub() {
      window.open("https://github.com/eef-g", "_blank");
    }

</script>


<div class="p-base">
    <div class="p-base-title">
        <h1>In-Progress Reimages</h1>
    </div>
    <div class="p-base-item" id="bar"></div>
    {#if showLoading}
      <LoadingObject />
    {/if}
    {#if !showLoading}
      {#await onMount}
        <p>Fetching tickets...</p>
      {:then ticket}
        <ReimageTable tickets={$tickets} bind:this={reimagetableComp} on:update = {updateTickets}/>
      {:catch error}
        <p>Something went wrong: {error.message}</p>
      {/await}
    {/if}
    <div class="p-base-inner"></div>

    <img class="cui-logo-icon" alt="" src={cuiLogo} />
</div>
<TicketButton on:tasks = {customListen}/>
<div class="EefIcon" on:click={showGithub}>
    <img alt="" src={eeficon} height="48px" width="48px" />
    <div class="hidden">Made By Ethan Gray</div>
</div>


<style>
    .EefIcon{
      position: absolute;
      bottom: 0;
      left: 0;
      margin-left: .5%;
    }

    .hidden {
      display: none;
    }

    .EefIcon:hover .hidden {
      display: block;
      position: absolute;
      bottom: 0;
      left: 0;
      margin-left: 2%;
      margin-bottom: 2%;
      background-color: #004c23;
      color: white;
      border-radius: 5px;
      padding: 5px;
      font-size: 12px;
      font-family: Arial, Helvetica, sans-serif;
    }

    .EefIcon:hover {
      cursor: pointer;
    }

    @keyframes shadow-pop-tr {
  0% {
    box-shadow: 0 0 rgba(62, 62, 62, 0.18), 0 0 rgba(62, 62, 62, 0.18),
      0 0 rgba(62, 62, 62, 0.18), 0 0 rgba(62, 62, 62, 0.18),
      0 0 rgba(62, 62, 62, 0.18), 0 0 rgba(62, 62, 62, 0.18),
      0 0 rgba(62, 62, 62, 0.18), 0 0 rgba(62, 62, 62, 0.18);
    transform: translateX(0) translateY(0);
  }
  to {
    box-shadow: 1px -1px rgba(62, 62, 62, 0.18), 2px -2px rgba(62, 62, 62, 0.18),
      3px -3px rgba(62, 62, 62, 0.18), 4px -4px rgba(62, 62, 62, 0.18),
      5px -5px rgba(62, 62, 62, 0.18), 6px -6px rgba(62, 62, 62, 0.18),
      7px -7px rgba(62, 62, 62, 0.18), 8px -8px rgba(62, 62, 62, 0.18);
    transform: translateX(-8px) translateY(8px);
  }
}

.p-base-item {
  position: absolute;
  width: 100.26%;
  top: 55.5px;
  right: -0.29%;
  left: 0.03%;
  border-top: 1px solid #ccd0d4;
  box-sizing: border-box;
  height: 3px;
  font-family: Arial, Helvetica, sans-serif;
}

.p-base-inner {
  position: absolute;
  height: 100vh;
  top: 0;
  left: 0;
  background-color: #004c23;
  width: 64px;
}

.cui-logo-icon {
  position: absolute;
  top: 12px;
  left: 16px;
  width: 32px;
  height: 32px;
  object-fit: cover;
}

.p-base {
  position: absolute;
  background-color: #fff;
  width: 100%;
  height: 100vh;
  left: 0;
  top: 0;
  overflow: hidden;
  text-align: left;
  font-size: var(--font-size-mini);
  color: var(--color-black);
  font-family: Arial, Helvetica, sans-serif;
}

.p-base-title{
  margin-left: 6%;
}

.p-base-title h1{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 24px;
  font-weight: 600;
  margin-top: 1%;
  margin-bottom: 1%;
  color: #313538;
  position: absolute;
  top: 2%
}

#bar {
  position: absolute;
  top: 8%;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #ccd0d4;
}

</style>