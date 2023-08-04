from FreshAPI.api import API
from .fresh_parser import Parser
import json, os, eel, threading, sys
global RUNNING

class CUI_Client:
    global RUNNING
    """
    Main class for the CUI FreshService client
    """
    api = None
    parser = None
    agent_dict = None
    WEBSITE_PATH = os.path.join(os.sep, os.path.dirname(os.path.realpath(__file__)), ".website", "GUI.html")
    gui_thread = None
    api_thread = None
    RUNNING = True

    def __init__(self) -> None:
        self.api = API()
        self.parser = Parser(self.api)
        self.agent_dict = self.ParseAgents()
        self.gui_thread = threading.Thread(target=self.OpenWebsite)
        self.gui_thread.start()
        pass

    def __del__(self) -> None:
        self.gui_thread.join()
        pass
    def OpenWebsite(self) -> None:
        """
        Opens the website
        """
        url = "file://" + self.WEBSITE_PATH
        eel.init('web')
        eel.start("index.html", close_callback=CloseWebsite)
        pass



    # Anything in the eel.expose is available to the website
    @eel.expose
    def close_python(*args):
        global RUNNING
        print("Closing Python Server")
        os._exit(0)

    
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

    #endregion

    #region TicketSaving

    def SaveTicket(self, ticket_id: int) -> None:
        """
        Saves the ticket to a file
        """
        ticket_data = {}
        raw_ticket_data = self.api.GetTicketInfo(ticket_id).json()
        
        ticket_data["ticket"] = raw_ticket_data
        ticket_data["tasks"] = self.ParseInProgressTasks( self.api.GetTicketTasks(ticket_id) )
        ticket_data["assigned_to"] = self.CheckAgent(ticket_data["ticket"]["ticket"]["responder_id"])
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
        print("Saving Reimage Tickets")
        reimage_tickets = self.api.GetTicketIDs("status:2 AND tag:\'Reimage\'")
        for ticket_id in reimage_tickets:
            self.SaveTicket(ticket_id)
    #endregion



def CloseWebsite(page, sockets_still_open):
    """
    Closes the website & stops the python code
    """
    print("Closing python backend")
    os._exit(0)