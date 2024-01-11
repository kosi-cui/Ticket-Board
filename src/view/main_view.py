from customtkinter import *
from src.controller.main_controller import MainController
from src.view.widgets import *

import os
from dotenv import load_dotenv

class MainView:
    def __init__(self):
        load_dotenv("../../.env")
        self.controller = MainController()
        user = os.getenv("API_KEY")
        url = os.getenv("HELPDESK_URL")
        self.controller.logIn(user, url)
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


        # Create the widgets
        self.createWidgets()
    

    def createWidgets(self):
        self.sidebar = Sidebar(self.root, self.controller)
        self.ticket_board = TicketBoard(self.root) # Add data later
        data = self.controller.getReimageTickets()
        self.ticket_board.updateData(data)

        
    def unloadWidgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()



    # Functions

    def runApp(self):
        # Start the main loop
        self.root.mainloop()
