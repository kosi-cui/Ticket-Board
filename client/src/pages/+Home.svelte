<script>
	// Component Imports
	import Sidebar from "../components/Sidebar.svelte";
	import TicketTable from "../components/TicketTable.svelte";

	// Globals
	let ticket_num = '30412';
	let tickets = [];

	function fetchTicket(ticket_number) {
		return fetch('/api/ticket/' + ticket_number)
			.then(r => r.json())
			.then(result => {
				return result;
		});
	}

	function addTicket() {
		fetchTicket(ticket_num).then(ticket => {
			// Get & Parse Tasks
			let ticket_tasks = ticket.tasks;
			let curr_tasks = [];
			if (ticket_tasks.length > 0) {
				curr_tasks = ticket_tasks.map(task => task);
			} else {
				curr_tasks = ['Execute Reimage Sequence'];
			}

			// Set up ticket object
			let curr_ticket = {
				agent: ticket.agent,
				title: ticket.title,
				created_at: ticket.created_at,
				tasks: curr_tasks
			};
			// Need to update via assignment & not push so svelte recognizes the change
			tickets = [...tickets, curr_ticket];
			console.log(tickets);
		});
	}
</script>

<style>
    .content {
        position: absolute;
        left: 5.1%;
        width: 94.9%;
        height: 100vh;
    }
</style>

<Sidebar topImage="" bottomImage="" />
<div class="content">
	<p> Ticket Number: </p>
	<br>
	<input type="text" bind:value={ticket_num} />
	<button on:click={addTicket}>Fetch Ticket</button>
	<br>
	<TicketTable {tickets} />
</div>