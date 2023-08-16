<script>
    import "$lib/fonts.css"
    import { writable } from "svelte/store";

    const tasks = writable([]);
    const id = writable("");
    const date = writable("");
    const assigned = writable("");
    const name = writable("");


    function updateTicket(){
        id.set(ticket.id);
        tasks.set(ticket.tasks);
        date.set(ticket.createdOn);
        assigned.set(ticket.assignedTo);
        name.set(ticket.name);
        $tasks.forEach(task => {
            console.log(task.status);
            if (task.status != 1) {
                $tasks.splice($tasks.indexOf(task), 1);
            }
        })
    }

    export let ticket

    $: ticket && updateTicket();
</script>

<tr>
    <td><input type="checkbox" name= "{$id}-cb" value="check"/></td>
    <td>{$name}</td>
    <td>
        <select name="{$id}-tasks">
            {#each ticket.tasks as task}
                <option value="{task.title}">{task.title}</option>
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
        font-family: 'Gandhi-Sans', sans-serif;
    }

    select {
        border-color: white;
        background-color: white;
        box-shadow: 0 0 0 0 white;
        text-align: left;
        font-family: 'Gandhi-Sans', sans-serif;
    }
</style>