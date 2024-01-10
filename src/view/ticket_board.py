from customtkinter import *
from tkinter import ttk

class TicketBoard():
    def __init__(self, root, data=[]):
        self.root = root
        self.data = data
        self.initialize()

    def initialize(self):
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0,)
        self.style.map('Treeview', background=[('selected', '#004c23')])
        self.style.configure("Treeview.Heading",
                        background="#004c23",
                        foreground="white",
                        borderwidth=0,
                        relief="flat")
        self.style.configure("Treeview.Heading",
                        background=[('active', "#004c23")])
        
        column_width = int(self.root.winfo_width() * 0.84 / 3.25)
        board_height = int(self.root.winfo_height() * 0.8 / 20)
        columns = ("ID", "Device", "Status", "Agent")
        self.table = ttk.Treeview(
            master=self.root,
            columns=columns,
            show="headings",
            height=board_height,
            selectmode="browse",
            style="Treeview"
        )
        self.table.column("ID", anchor="c", width=column_width)
        self.table.column("Device", anchor="w", width=column_width)
        self.table.column("Status", anchor="w", width=column_width)
        self.table.column("Agent", anchor="w", width=column_width)
        self.table.heading("ID", text="ID")
        self.table.heading("Device", text="Device")
        self.table.heading("Status", text="Status")
        self.table.heading("Agent", text="Agent")

        
        # self.root.grid_columnconfigure(1, weight=1)
        # self.root.grid_rowconfigure(0, weight=1)