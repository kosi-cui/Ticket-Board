<script type="ts">
    import {invoke} from "@tauri-apps/api";

    async function updateTickets() {
        await invoke("updateTickets");
    }
</script>

<div class="TicketButton">
    <button type="button" on:click={updateTickets}> Update Tickets</button>
</div>

<style lang="css">
    .TicketButton{
        font-family: "Ghandi-Sans", sans-serif; 
        visibility: visible;
        position: absolute;
        right: 0;
        bottom: 0;
        margin-bottom: 1%;
        margin-right: 1%;
    }

    .TicketButton button{
        background-color: #004c23;
        color: white;
        border: none;
        border-radius: 10px 10px 10px 10px;
        padding: 2vh 3vh;
        font-size: 18px;
        box-shadow: 0 7px #999;
    }

    .TicketButton button:hover{
        background-color: #003012;
    }

    .TicketButton button:active{
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
</style>