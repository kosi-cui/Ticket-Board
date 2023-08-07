import requests, os, json

class API():
    """
    Class used for interacting with the FreshService API.
    """
    API_KEY = -1
    URL = -1
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_PATH = os.path.join(os.sep, CURR_DIR, ".credentials", "conf")

    def __init__(self):
        self.Init()

    #region API_Setup

    def Init(self):
        if not os.path.exists(os.path.join(os.sep, self.CURR_DIR, ".credentials")):
            os.mkdir(os.path.join(os.sep, self.CURR_DIR, ".credentials"))

        if not os.path.exists(self.CONFIG_PATH):
            print("Please enter your FreshService API key: ")
            key = input()
            print("Please enter the base FreshService URL (e.g. https://helpdesk.freshservice.com): ")
            url = input()
            with open(self.CONFIG_PATH, 'w') as f:
                f.write(f"Key: {key}\n")
                f.write(f"URL: {url}/api/v2\n")
            print("Login info saved to " + self.CONFIG_PATH)
        self.ReadConfig()


    def ReadConfig(self):
        with open(self.CONFIG_PATH, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "Key" in line:
                    self.API_KEY = line.split(" ")[1].strip('\n')
                if "URL" in line:
                    self.URL = line.split(" ")[1].strip('\n')

        if(self.API_KEY == -1):
            print("Error: API key not found in config file")
            exit(1)
        if(self.URL == -1):
            print("Error: URL not found in config file")
            exit(1)

    #endregion

    #region TicketFunctions

    def GetTicketInfo(self, ticket_id, args = []):
        # Create the URL for the specified ticket + args

        # The responder_id is the person who currently has the ticket.
        # TODO: Add a way to get the name of the responder_id
        url = self.URL + f"/tickets/{str(ticket_id)}"
        if(len(args) > 0):
            url +="?include="
            for arg in args:
                url += arg

        # Get the ticket info
        response = requests.get(url, auth = (self.API_KEY, "X"))
        return response

    def GetTicketIDs(self, query: str) -> list:
        """
        Gets the ticket IDs for a given query
        """
        url = self.URL + f"/tickets/filter?query=\"{query}\""
        response = requests.get(url, auth = (self.API_KEY, "X"))
        ticket_ids = []
        for ticket in response.json()["tickets"]:
            ticket_ids.append(ticket["id"])
        return ticket_ids

    def GetTicketTasks(self, ticket_id):
        # Status 3 == Closed, Status 1 == Unresolved
        url = self.URL + f"/tickets/{str(ticket_id)}" + "/tasks"
        response = requests.get(url, auth = (self.API_KEY, "X"))
        return response.json()

    def UpdateTicketTask(self, ticket_id, task_id, status):
        # API Documentation: https://api.freshservice.com/#update_a_ticket_task
        
        # Status 3 == Closed, Status 1 == Unresolved
        url = self.URL + str(ticket_id) + "/tasks/" + str(task_id)
        
        # For the data, we want to be able to grab the current task info, and then update the status.
        # TODO: Add a way to get the current task info and update the status
        data = {"status": status}
        response = requests.put(url, auth = (self.API_KEY, "X"), data = data)
        return response

    #endregion


    #region AgentFunctions

    def GetAgents(self, query=[]):
        url = self.URL + "/agents"
        if(len(query) > 0):
            url += "?query=\""
            for q in query:
                url += q
            url += "\""
        response = requests.get(url, auth = (self.API_KEY, "X"))
        return response.json()

    #endregion
