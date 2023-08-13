<script lang="ts">
    import {invoke} from "@tauri-apps/api";

    import ReimageRow from "./ReimageRow.svelte";

    const tempTasks : Record<string, any>[] = 
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

    // Right now this array is just a placeholder for the data that will be returned from the Rust API
    export let tickets : Record<string, any>[] = [
      {
        id: "0001",
        tasks: tempTasks,
        createdOn: "01/01/2021",
        assignedTo: "John Doe"
      },
      {
        id: "0002",
        tasks: tempTasks,
        createdOn: "01/01/2021",
        assignedTo: "John Doe"
      },
    {
        id: "0003",
        tasks: tempTasks,
        createdOn: "01/01/2021",
        assignedTo: "John Doe"
      },
      {
        id: "0004",
        tasks: tempTasks,
        createdOn: "01/01/2021",
        assignedTo: "John Doe"
      }
    ]
    console.log(typeof tickets);
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
        {#each tickets as ticket}
          <ReimageRow ticket={ticket}/>
        {/each}
    </tbody>
</table>


<style>

table {
  visibility: visible;
  border-collapse: collapse;
  width: 90%;
  margin-left: 10%;
  margin-top: 3%;
  font-size: 16px;
  font-family: 'Gandhi-Sans', 'Times New Roman', Times, serif;
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
}


</style>