// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}

declare class Task {
	id: string;
	name: string;
}

declare class Ticket {
	id: string;
	tasks: Task[];
	createdOn: string;
	assignedTo: string;
}