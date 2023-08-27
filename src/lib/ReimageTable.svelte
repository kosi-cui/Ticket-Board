<script>
    import {invoke} from "@tauri-apps/api";
    import { writable } from "svelte/store";

    import ReimageRow from "./ReimageRow.svelte";

    const tempTasks = 
    [
        {
            name: "Label",
            id: 0
        },
        {
            name: "Decrypt",
            id: 1
        },
        {
           name: "Reimage",
           id: 2
        }
    ]

    const ticketArray = writable([]);
    // Right now this array is just a placeholder for the data that will be returned from the Rust API
    export let tickets 

    function convertTickets(ticketInput){
        ticketArray.set(ticketInput);
    }

    $: tickets && convertTickets(tickets);
    let trigger = false;

    export function testListen(event){
        console.log("testListen");
        trigger = !trigger;
    }

</script>



<table id="ReimageTable">
    <thead>
        <tr>
            <th> </th>
            <th>&nbsp;Subject</th>
            <th>&nbsp;Step</th>
            <th>&nbsp;Date Created</th>
            <th>&nbsp;Assigned To</th>
        </tr>
    </thead>

    <tbody>
      {#await tickets}
      {:then tickets}
       {#each tickets as ticket}
          <ReimageRow ticket={ticket} updateTrigger={trigger} on:update/>
        {/each}
      {/await}
    </tbody>
</table>



<style>

table {
  visibility: visible;
  border-collapse: collapse;
  width: 1800px;
  margin-left: 10%;
  margin-top: 3%;
  font-size: 16px;
  font-family: Arial, Helvetica, sans-serif;
  overflow-y: scroll;
  overflow-x: scroll;
  display: block;
  position: absolute;
  top: 5%;
  left: -5%;
}

:global(th:nth-child(1), th:nth-child(2), th:nth-child(3), th:nth-child(4), th:nth-child(5)
        td:nth-child(1), td:nth-child(2), td:nth-child(3), td:nth-child(4), td:nth-child(5)) {
  width: 445px;
}

table th:first-child {
  border-radius: 10px 0 0 10px;
  border-right: solid #cfd7df 3px;
}

table th:last-child{
  border-right: none;
}

thead {
  background: #ebeff3;
  text-align: left;
}

th {
  position: sticky;
  border-right: solid #cfd7df 2px;
  height: 40px;
  font-size: large;
  font-family: Arial, Helvetica, sans-serif;
  width: auto;
}

</style>