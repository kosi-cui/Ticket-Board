from customtkinter import *
from src.controller.main_controller import MainController

class Sidebar:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.initialize()

    def initialize(self):
        self.frame = CTkFrame(
            master=self.root,
            fg_color=self.controller.getAcColor(),
            border_color=self.controller.getAcColor(),
            corner_radius=0
        )
        self.frame.place(relx = 0, rely = 0, relwidth = 0.16, relheight = 1)

        # Create the sidebar buttons
        sidebar_buttons = []
        sidebar_buttons.append(
            CTkButton(
                master=self.frame,
                text="Home",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.home_button
            )
        )
        sidebar_buttons.append(
            CTkButton(
                master=self.frame,
                text="Tickets",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.tickets_button
            )
        )
        sidebar_buttons.append(
            CTkButton(
                master=self.frame,
                text="Settings",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.settings_button
            )
        )
        sidebar_buttons.append(
            CTkButton(
                master=self.frame,
                text="Exit",
                fg_color=self.controller.getAcColor(),
                border_color=self.controller.getAcColor(),
                corner_radius=0,
                command=self.end_app
            )
        )
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        for i in range(len(sidebar_buttons)):
            sidebar_buttons[i].grid(
                row=i//2, column=i%2, sticky="ew", padx=1, pady=1
            )


    # Button Functions
    def settings_button(self):
        print("Settings Button Pressed")

    def home_button(self):
        print("Home Button Pressed")

    def tickets_button(self):
        print("Tickets Button Pressed")        
    
    def end_app(self):
        self.root.destroy()