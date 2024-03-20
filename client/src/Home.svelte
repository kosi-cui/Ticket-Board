<script>
	// Globals
	let ticket_num = '30028';
	let ticket_agent = 'null';
	let ticket_title = 'null';
	let ticket_date = 'null';
	let ticket_tasks = ['None'];

	function fetchTicket(ticket_number) {
		return fetch('/api/ticket/' + ticket_number)
			.then(r => r.json())
			.then(result => {
				return result;
		});
	}

	function parseTicket() {
		fetchTicket(ticket_num).then(ticket => {
			console.log(ticket);
			ticket_agent = ticket.agent;
			ticket_title = ticket.title;
			ticket_date = ticket.created_at;
			ticket_tasks = ticket.tasks;
			if (ticket_tasks.length > 0) {
				ticket_tasks = ticket_tasks.map(task => task);
			} else {
				ticket_tasks = ['Execute Reimage Sequence'];
			}
		});
	}
</script>

<p>Ticket Number:</p>
<input type="text" id="ticket_number" name="ticket_number" bind:value={ticket_num}>
<button on:click={parseTicket}>Get ticket info</button>
<br>
<h1>Ticket Info: </h1>
<p>
	Agent: {ticket_agent}
	<br>
	Title: {ticket_title}
	<br>
	Date: {ticket_date}
	<br>
	Tasks: <select>
		{#each ticket_tasks as task, index (task)}
			<option selected={index === 0}>{task}</option>
		{/each}
	</select>
</p>