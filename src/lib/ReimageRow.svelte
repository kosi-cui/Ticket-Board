<script lang="ts">
    import "$lib/fonts.css"

    const delay = ms => new Promise(res => setTimeout(res, ms));

    export let ticket: Record<string, any> = {
        id: "0001",
        tasks: [
            {
                name: "Label",
                id: "0"
            },
            {
                name: "Decrypt",
                id: "1"
            }
        ],
        createdOn: "01/01/2021",
        assignedTo: "John Doe"
    }

    let id = ticket.id;
    let date = ticket.createdOn;
    let assigned = ticket.assignedTo;
</script>

<tr>
    <td><input type="checkbox" name= "{id}-cb" value="check"/></td>
    <td>INC-{id}</td>
    <td>
        <select name="{id}-tasks">
            {#each ticket.tasks as task}
                <option value="{task.name}">{task.name}</option>
            {/each}
        </select>
    </td>
    <td>{date}</td>
    <td>{assigned}</td>
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