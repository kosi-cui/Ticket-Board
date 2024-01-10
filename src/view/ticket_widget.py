from customtkinter import *

class TicketWidget(CTkFrame):
    def __init__(self, root, name, tasks, agent, width, **kwargs):
        super().__init__(master=root, **kwargs)
        print(width)
        
        self.ticket_name = CTkLabel(master=self, text=name, font=("Arial", 18))
        self.ticket_name.grid(row=0, column=1, padx=(10, 0))   

        self.ticket_tasks = CTkComboBox(
            master=self, 
            values=tasks,
            state="readonly",
            button_color="white",
            border_color="white")
        self.ticket_tasks.set(tasks[0])
        self.ticket_tasks.grid(row=0, column=2, padx=(width/8, 0))  # Modify this line

        self.ticket_agent = CTkLabel(master=self, text=agent)
        self.ticket_agent.grid(row=0, column=3, padx=(width/8, 0))  # Modify this line


        self.check_box = CTkCheckBox(master=self, text="Mark as Complete")
        self.check_box.grid(row=0, column=4, sticky="e", padx=(width/6, 0))