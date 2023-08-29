<script>
    import { invoke } from "@tauri-apps/api";
    import { writable } from "svelte/store";
    import { createEventDispatcher } from "svelte";

    const tasks = writable([]);
    const id = writable("");
    const date = writable("");
    const assigned = writable("");
    const name = writable("");
    let selectedTask = "";
    let options = [];
    let originalTask = "";
    let finished = false;

    let dispatch = createEventDispatcher();

    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function updateTicket(){
        id.set(ticket.id);
        tasks.set(ticket.tasks);
        date.set(ticket.createdOn);
        assigned.set(ticket.assignedTo);
        name.set(ticket.name);
        $tasks.forEach(task => {
            if (task.status != 1) {
                $tasks.splice($tasks.indexOf(task), 1);
            }
        });
        if($tasks.length > 0) {
            Object.entries(Object.values($tasks)).forEach(task => {
                Object.values(task).forEach(element => {
                    if(element["title"] != undefined)
                        options.push(element["title"]);
                });
            });
        }
        selectedTask = options[0];
        originalTask = selectedTask;
    }   

    async function closeTask(){
        if(selectedTask == originalTask && !finished)
            return; 
        if (finished) {
            console.log("Resolving ticket " + $id);
            await invoke("resolve_ticket", {ticketId: $id, agentId: ticket.agentId});
        }
        else
        {  
            Object.entries(Object.values($tasks)).forEach(task => {
                    Object.values(task).forEach(element => {
                        if(element["title"] != undefined && element["title"] == selectedTask && element["id"] != 0)
                        {
                            invoke("close_ticket_task", {ticketId: $id, taskId: element["id"]});
                        }
                    });
                });
        }
        await delay(2000);
        if (finished)
            dispatch("update",
            {
                resolved: $id,
            });
        else
            dispatch("update", 
        {
            resolved: -1,
        });
    }

    export let ticket;
    export let updateTrigger = false;


    $: ticket && updateTicket();
    $: updateTrigger && closeTask();
</script>

<tr>
    <td><input type="checkbox" name= "{$id}-cb" value="check" bind:checked={finished}/></td>
    <td>{$name}</td>
    <td>
        <select bind:value={selectedTask} on:click = "{() => console.log(selectedTask)}">
            {#each options as value}
                <option {value}>{value}</option>
            {/each}
        </select>
    </td>
    <td>{$date}</td>
    <td>{$assigned}</td>
</tr>


<style>
    tr:hover {
        background-color: #f2f7fc;
    }

    tr td:first-child{
        border-right: solid #cfd7df 3px;
    }

    tr{
        border-bottom: solid #ebeff3 .25px;
        font-family: Arial, Helvetica, sans-serif;
        font-size: large;
        height: 40px;
    }

    select {
        border-color: white;
        background-color: white;
        box-shadow: 0 0 0 0 white;
        text-align: left;
        font-family: Arial, Helvetica, sans-serif;
        font-size: large;
    }

    input {
        size: 2rem;
    }
</style>