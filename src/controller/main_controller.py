from src.model.main_model import MainModel
# TODO: Incorporate the model into the controller. 
#       The controller should be the only thing that interacts with the model.
#       The view should only interact with the controller.


class MainController:
    def __init__(self):
        self.data = MainModel()

    # Getters
    def getTitle(self):
        return self.data.config.title
    def getGeometry(self):
        return self.data.config.geometry
    def getBgColor(self):
        return self.data.config.bg_color
    def getAcColor(self):
        return self.data.config.ac_color

    # Setters
    def logIn(self, key, url):
        return self.data.config.logIn(key, url)

    def changeAPIUser(self, key):
        return self.data.config.changeAPIUser(key)

    def changeAPIUrl(self, url):
        return self.data.config.changeAPIUrl(url)   
    

    # Functions
    def button_function(self):
        print("Hello World!")