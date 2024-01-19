import requests

class APIAgent:
    def __init__(self, key=None, url=None):
        self.key = key
        self.url = url
        self.current_ticket = None
        self.filtered_ticket_list = None
        if self.url != None and self.key != None:
            self.valid_user = self.validKey()
        else:
            self.valid_user = False
        self.users = None


    def validKey(self) -> bool:
        url = self.url + "/api/v2/tickets.json"
        response = requests.get(url, auth=(self.key, "X"))
        if response.status_code == 200:
            return True
        else:
            return False



    # Setters
    def setKey(self, key):
        self.key = key
        if self.url != None:
            self.valid_user = self.validKey()


    def setUrl(self, url):
        self.url = url
        if self.key != None:
            self.valid_user = self.validKey()


    # Decorators
    def authMethod(func):
        def wrapper(self, *args, **kwargs):
            if not self.valid_user:
                return None
            return func(self, *args, **kwargs)
        return wrapper


    def reqTicket(func):
        def wrapper(self, *args, **kwargs):
            if self.current_ticket == None:
                return None
            return func(self, *args, **kwargs)
        return wrapper



    # Ticket Functions -- Requires valid API Key & URL
    @authMethod
    def ticketGetRequest(self, ticket_id):
        url = self.url + "/api/v2/tickets/" + str(ticket_id) + ".json"
        response = requests.get(url, auth=(self.key, "X"))
        if response.status_code == 200:
            self.current_ticket = response.json()["ticket"]
            return response.json()
        elif response.status_code == 404:
            return {"error": "Ticket not found."} 
        

    @authMethod
    def filteredTicketGetRequest(self, filter):
        if filter[0] != '"':
            filter = f'"{filter}'
        if filter[-1] != '"':
            filter = f'{filter}"'
        url = self.url + f'/api/v2/tickets/filter?query={filter}'
        response = requests.get(url, auth=(self.key, "X"))
        if response.status_code == 200:
            self.filtered_ticket_list = response.json()["tickets"]
            return response.json()["tickets"]
        elif response.status_code == 404:
            return {"error": "Filter not found."}


    @authMethod
    def ticketPostRequest(self, ticket_id, data):
        if self.validKey() == False:
            return None
        url = self.url + "/api/v2/tickets/" + str(ticket_id) + ".json"
        response = requests.post(url, auth=(self.key, "X"), data=data)
        return response.json()
    

    @authMethod
    def ticketPutRequest(self, ticket_id, data):
        if self.validKey() == False:
            return None
        url = self.url + "/api/v2/tickets/" + str(ticket_id) + ".json"
        response = requests.put(url, auth=(self.key, "X"), data=data)
        return response.json()
    
    
    @authMethod
    def getGroupUsers(self, group_id):
        url = self.url + "/api/v2/groups"
        response = requests.get(url, auth=(self.key, "X"))
        if response.status_code == 200:
            groups_raw = response.json()
            groups_raw = groups_raw["groups"]
            specific_group = None
            for group in groups_raw:
                if group["id"] == int(group_id):
                    specific_group = group["members"]
            return specific_group
        elif response.status_code == 404:
            return {"error": "Group not found."}

    @authMethod
    def getAllUsers(self):
        url = self.url + "/api/v2/agents"
        response = requests.get(url, auth=(self.key, "X"))
        if response.status_code == 200:
            self.users = response.json()["agents"]
        elif response.status_code == 404:
            return {"error": "Group not found."}

    # Parsed Data Functions
    @reqTicket
    def getTicketTitle(self):
        title = self.current_ticket["subject"]
        return title

    @reqTicket
    def getTicketDescription(self):
        description = self.current_ticket["ticket"]["description"]
        return description

    @reqTicket
    def getTicketTags(self):
        tags = self.current_ticket["ticket"]["tags"]
        return tags
    
    def getUser(self, id):
        if self.users == None:
            return None
        for user in self.users:
            if user["id"] == id:
                return f"{user["first_name"]} {user["last_name"]}"
        return None