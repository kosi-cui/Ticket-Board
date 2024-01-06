from model.config import Config

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