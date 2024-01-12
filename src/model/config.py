from src.model.api_agent import APIAgent
import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        self.title = "ReimageBoard"
        self.geometry = "1280x720"
        self.bg_color = "white"
        self.ac_color = "#004c23"
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

    def updateAgentDict(self):
        load_dotenv("../../.env")
        it_group_id = os.getenv("IT_GROUP_ID")  
        agent_ids = self.api_agent.getGroupUsers(it_group_id)
        self.api_agent.getAllUsers()
        agent_names = [self.api_agent.getUser(agent_id) for agent_id in agent_ids]
        self.agent_dict = dict(zip(agent_ids, agent_names))
        self.api_agent.users = None

    # Getters
    def getCurrentTicket(self) -> dict:
        return self.api_agent.current_ticket
    
    def getFilteredTicketList(self) -> list:
        return self.api_agent.filtered_ticket_list
    
    def getAgentDict(self) -> dict:
        return self.agent_dict
    