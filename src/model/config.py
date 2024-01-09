from src.model.api_agent import APIAgent

class Config:
    def __init__(self):
        self.title = "ReimageBoard"
        self.geometry = "400x240"
        self.bg_color = "white"
        self.api_agent = APIAgent()
    


    # Setters 
    def logIn(self, key, url) -> bool:
        # Eventually wil be read from a config file. For now, use the .env
        self.api_agent.setKey(key)
        self.api_agent.setUrl(url)
        return self.api_agent.valid_user
    

    def changeAPIUser(self, key) -> bool:
        self.api_agent.setKey(key)
        return self.api_agent.valid_user


    def changeAPIUrl(self, url) -> bool:
        self.api_agent.setUrl(url)
        return self.api_agent.valid_user
    


    # Getters
    def getCurrentTicket(self) -> dict:
        return self.api_agent.current_ticket
    
    def getFilteredTicketList(self) -> list:
        return self.api_agent.filtered_ticket_list
    