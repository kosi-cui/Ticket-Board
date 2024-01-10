from customtkinter import *
from src.controller.main_controller import MainController
from CTkTable import *
from tkinter import ttk

import os
from dotenv import load_dotenv

class MainView:
    def __init__(self):
        load_dotenv("../../.env")
        self.controller = MainController()
        #TODO: Have a controller.loadConfig() function that loads the config from a file
        self.root = None
        self.appSetup()
    

    def appSetup(self):
        # Create the root window
        self.root = CTk()
        self.root.title(self.controller.getTitle())
        self.root.geometry(self.controller.getGeometry())
        
        # Make the window borderless and fullscreen
        self.root.overrideredirect(True)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Bind F11 to toggle fullscreen mode
        self.root.bind('<F11>', self.end_app)

        # Create the widgets
        self.createWidgets()
    

    def createWidgets(self):
        sidebar = CTkFrame(
            master=self.root,
            fg_color=self.controller.getAcColor(), 
            border_color=self.controller.getAcColor(),
            corner_radius=0
        )
        sidebar.place(relx = 0, rely = 0, relwidth = 0.16, relheight = 1)
        
        # Create the sidebar buttons
        sidebar_buttons = []
        sidebar_buttons.append(
            CTkButton(
                master=sidebar,
                text="Home",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.controller.button_function
            )
        )
        sidebar_buttons.append(
            CTkButton(
                master=sidebar,
                text="Tickets",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.controller.button_function
            )
        )
        sidebar_buttons.append(
            CTkButton(
                master=sidebar,
                text="Settings",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.controller.button_function
            )
        )
        sidebar_buttons.append(
            CTkButton(
                master=sidebar,
                text="Exit",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.end_app
            )
        )
        for i in range(len(sidebar_buttons)):
            sidebar_buttons[i].grid(row=i//2, column=i%2, sticky="ew", padx=2, pady=2)



        # Create the ticket board
        ticket_board = CTkScrollableFrame(
            master=self.root,
            fg_color="blue",
            corner_radius=0
        )
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=("Arial", 12)
        )
        style.map('Treeview', background=[('selected', '#004c23')])
        style.configure("Treeview.Heading",
                        background="#004c23",
                        foreground="white",
                        borderwidth=0,
                        relief="flat")
        style.configure("Treeview.Heading",
                        background=[('active', "#004c23")])


        board_width = int(self.root.winfo_width() * 0.84 / 3.25)
        board_height = int(self.root.winfo_height() * 0.8 / 20)

        ticket_board.place(relx = 0.16, rely = 0.2, relwidth = 0.84, relheight = 0.8)
        # Test values for the ticket board
        columns = ("id", "Device", "Status", "Agent")
        table = ttk.Treeview(
            master=ticket_board,
            columns=columns,
            show="headings",
            height=board_height,
            selectmode="browse",
            style="Treeview"
        )
        table.column("id", anchor="c", width=board_width)
        table.column("Device", anchor="w", width=board_width)
        table.column("Status", anchor="w", width=board_width)
        table.column("Agent", anchor="w", width=board_width)
        table.heading("id", text="id")
        table.heading("Device", text="Device")
        table.heading("Status", text="Status")
        table.heading("Agent", text="Agent")
        table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


        
    def unloadWidgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()



    # Functions

    def runApp(self):
        # Start the main loop
        self.root.mainloop()

    def end_app(self, event=None):
        self.root.destroy()