from FreshAPI.api import API
import os, json

class Parser():
    """
    Takes raw data from the API class and makes it readable
    """
    api = None
    TICKET_FOLDER = ".tickets"

    def __init__(self, api_obj: API) -> None:
        temp_dir = api_obj.CURR_DIR.replace("FreshAPI", "|")
        main_dir = f"{temp_dir.split('|')[0]}web"
        print(main_dir)
        self.TICKET_FOLDER = os.path.join(os.sep, main_dir, self.TICKET_FOLDER)
        if not os.path.exists(self.TICKET_FOLDER):
            os.mkdir(self.TICKET_FOLDER)
            with open (os.path.join(self.TICKET_FOLDER, "README"), 'w') as f:
                f.write("This folder contains ticket data. Do not delete.")
        self.api = api_obj
        pass
    


    def GetRawAgents(self, query=[]) -> dict:
        """
        Gets the raw agent data
        """
        return self.api.GetAgents(query=query).json()
    
    def RefineAgentsData(self, rawAgentData: dict) -> dict:
        """
        Gets the refined agent data
        """
        refined_agents = {}
        for agent in rawAgentData["agents"]:
            refined_agents[int(agent["id"])] = f"{agent['first_name']} {agent['last_name']}"
        return refined_agents
    
    
    def GetRefinedTicketTasks(self, ticket_id: int) -> dict:
        """
        Gets the tasks for a ticket and refines them
        """
        raw_tasks = self.GetRawTicketTasks(ticket_id)
        refined_tasks = {}
        for task in raw_tasks:
            refined_tasks[task["id"]] = task
        return refined_tasks
    
