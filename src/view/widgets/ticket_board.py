from customtkinter import *
from tkinter import ttk

class TicketBoard():
    def __init__(self, root, data=[]):
        self.root = root
        self.data = data
        self.initialize()

    def initialize(self):
        # Background setup
        self.frame = CTkScrollableFrame(
            master=self.root,
            fg_color="blue",
            corner_radius=0
        )
        self.board_width = int(self.root.winfo_width() * 0.84 / 3.25)
        self.board_height = int(self.root.winfo_height() * 0.8 / 20)
        self.frame.place(relx = 0.16, rely = 0.2, relwidth = 0.84, relheight = 0.8)
        
        # Table setup
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        # background="#2a2d2e",
                        # foreground="white",
                        rowheight=50,
                        # fieldbackground="#343638",
                        # bordercolor="#343638",
                        borderwidth=0,
                        font=("Arial", 18)
        )
        # style.map('Treeview', background=[('selected', '#004c23')])
        style.configure("Treeview.Heading",
                        # background="#004c23",
                        # foreground="white",
                        borderwidth=0,
                        relief="flat",
                        font=("Arial", 20))
        columns = ("id", "Device", "Status", "Agent")
        self.table = ttk.Treeview(
            master=self.frame,
            columns=columns,
            show="headings",
            height=self.board_height,
            selectmode="browse",
            style="Treeview"
        )
        self.table.column("id", anchor="c", width=self.board_width)
        self.table.column("Device", anchor="w", width=self.board_width)
        self.table.column("Status", anchor="w", width=self.board_width)
        self.table.column("Agent", anchor="w", width=self.board_width)
        self.table.heading("id", text="id")
        self.table.heading("Device", text="Device")
        self.table.heading("Status", text="Status")
        self.table.heading("Agent", text="Agent")
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


    # Functions
    def updateData(self, data):
        self.data = data
        self.updateTable()

    def addData(self, data):
        self.data.append(data)
        self.updateTable()

    def clearData(self):
        self.data = []
        self.updateTable()


    # Table Functions
    def updateTable(self):
        self.table.delete(*self.table.get_children())
        for i in range(len(self.data)):
            self.table.insert("", "end", values=self.data[i])
        self.table.update_idletasks()
        self.table.update()
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.frame.update_idletasks()
        self.frame.update()
        self.frame.place(relx = 0.16, rely = 0.2, relwidth = 0.84, relheight = 0.8)