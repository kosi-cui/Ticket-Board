from src.model.config import Config
# TODO: Incorporate the model into the controller. 
#       The controller should be the only thing that interacts with the model.
#       The view should only interact with the controller.


class MainController:
    def __init__(self):
        self.config = Config()


    # Getters
    def getTitle(self):
        return self.config.title
    def getGeometry(self):
        return self.config.geometry
    def getBgColor(self):
        return self.config.bg_color
    

    # Public Functions
    def button_function(self):
        print("Button Pressed")

    def printReimageTickets(self):
        for ticket in self.config.api_agent.filtered_ticket_list:
            if "subject" in ticket:
                print(f"#INC-{ticket["id"]}: {ticket["subject"]}")