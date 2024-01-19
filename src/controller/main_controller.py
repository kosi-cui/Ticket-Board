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
    def getReimageTickets(self):
        return self.prepTicketData()

    # Setters
    def logIn(self, key, url):
        return self.data.config.logIn(key, url)

    def changeAPIUser(self, key):
        return self.data.config.changeAPIUser(key)

    def changeAPIUrl(self, url):
        return self.data.config.changeAPIUrl(url)   
    
    

    # Functions
    def prepTicketData(self):
        self.data.config.updateAgentDict()
        data = self.data.config.api_agent.filteredTicketGetRequest("tag:Reimage")
        parsed_data = [(ticket["id"], self.parseDeviceName(ticket["subject"]), "Decrypt Bitlocker", self.parseAgentId(ticket["responder_id"])) for ticket in data]
        return parsed_data

    def parseDeviceName(self, subject):
        start = subject.find(" - ")
        end = subject.find(" - ", start + 1)
        if end == -1:
            end = len(subject)
        return subject[start + 3:end]
    
    def parseAgentId(self, agent_id):
        return self.data.config.agent_dict[agent_id]