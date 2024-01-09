from customtkinter import *
from src.controller.main_controller import MainController
import os
from dotenv import load_dotenv

class MainView:
    def __init__(self):
        load_dotenv("../../.env")
        self.controller = MainController()
        self.root = None
        self.appSetup()
    

    def appSetup(self):
        # Visual Setup
        set_appearance_mode("light")
        set_default_color_theme("blue")

        # Create the root window
        self.root = CTk()
        self.root.title(self.controller.getTitle())
        self.root.geometry(self.controller.getGeometry())

        # Create the widgets
        self.createWidgets()
    
    def createWidgets(self):
        button = CTkButton(master=self.root, text="Hello World", command=self.controller.button_function)
        button.place(relx = 0.5, rely = 0.5, anchor = CENTER)


    def runApp(self):
        # Start the main loop
        self.root.mainloop()