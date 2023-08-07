from FreshAPI.api import API
from .fresh_parser import Parser
import json, os

class CUI_Client:
    """
    Main class for the CUI FreshService client
    """
    api = None
    parser = None
    agent_dict = None

    def __init__(self) -> None:
        self.api = API()
        self.parser = Parser(self.api)
        self.agent_dict = self.ParseAgents()
        pass

    #region eel_functions

    def Eel_ExposeTickets(self) -> list:
        """
        Exposes the tickets to the website
        """
        print("[PY] Exposing tickets")
        self.SaveReimages()
        return [f"./.tickets/{x}" for x in os.listdir(self.parser.TICKET_FOLDER) if x.endswith(".json")]
        #return [f"{self.parser.TICKET_FOLDER}{os.sep}{x}" for x in os.listdir(self.parser.TICKET_FOLDER) if x.endswith(".json")]
    
    def Eel_Print(self, message: str):
        """
        Prints a message to the console
        """
        print(f"[JS] {message}")
    
    #endregion



    
    #region ParserCalls

    def ParseAgents(self) -> dict:
        """
        Gets the refined agent data
        """
        return self.parser.RefineAgentsData( self.api.GetAgents(query=["department_id:19000169805"]) )
    
    def ParseTicketTasks(self, ticket_id: int) -> dict:
        """
        Gets the tasks for a ticket and refines them
        """
        return self.parser.GetRefinedTicketTasks(ticket_id)

    def ParseInProgressTasks(self, tasks: dict) -> dict:
        """
        Gets the tasks that are in progress
        """
        in_progress_tasks = {}
        for task in tasks["tasks"]:
            if task["status"] == 1:
                in_progress_tasks[task["id"]] = task
        return in_progress_tasks

    def GetWebData(self, ticket_dict: dict) -> dict:
        """
        Gets the web data for the ticket
        """
        output_dict = {}
        output_dict["name"] = f"INC-{ticket_dict['ticket']['ticket']['id']}"
        output_dict["steps"] = [x["title"] for x in ticket_dict["tasks"].values()]
        output_dict["assigned_to"] = self.agent_dict[int(ticket_dict["ticket"]["ticket"]["responder_id"])]
        raw_creation_date = ticket_dict["ticket"]["ticket"]["created_at"]
        creation_date = f"{raw_creation_date[5:7]}/{raw_creation_date[8:10]}/{raw_creation_date[0:4]}"
        output_dict["creation_date"] = creation_date
        return output_dict
    #endregion

    #region TicketSaving

    def SaveTicket(self, ticket_id: int) -> None:
        """
        Saves the ticket to a file
        """
        ticket_data = {}
        raw_ticket_data = self.api.GetTicketInfo(ticket_id).json()
        
        # Format the JSON file to have the data we want
        ticket_data["ticket"] = raw_ticket_data
        ticket_data["tasks"] = self.ParseInProgressTasks( self.api.GetTicketTasks(ticket_id) )
        ticket_data["assigned_to"] = self.CheckAgent(ticket_data["ticket"]["ticket"]["responder_id"])
        ticket_data["web_data"] = self.GetWebData(ticket_data)

        with open(os.path.join(self.parser.TICKET_FOLDER, f"INC-{str(ticket_id)}.json"), 'w') as f:
            json.dump(ticket_data, f, indent=4)
        pass

    def CheckAgent(self, agent_id: int) -> str:
        """
        Checks if the agent is in the agent dictionary
        """
        if agent_id in self.agent_dict:
            return self.agent_dict[agent_id]
        else:
            return "Unknown/Deleted Agent"


    def SaveReimages(self):
        """
        Saves all current reimage tickets to the .tickets folder
        """
        print("[PY] Saving reimage tickets")
        reimage_tickets = self.api.GetTicketIDs("status:2 AND tag:\'Reimage\'")
        for ticket_id in reimage_tickets:
            self.SaveTicket(ticket_id)
    #endregion