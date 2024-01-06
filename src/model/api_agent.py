import requests
import json

class APIAgent:
    def __init__(self, key=None, url=None):
        self.key = key
        self.url = url

    # Setters
    def setKey(self, key):
        self.key = key
    def setUrl(self, url):
        self.url = url

    def ticketGetRequest(self, ticket_id):
        url = self.url + "/api/v2/tickets/" + str(ticket_id) + ".json"
        response = requests.get(url, auth=(self.key, "X"))
        return response.json()
    
    def ticketPostRequest(self, ticket_id, data):
        url = self.url + "/api/v2/tickets/" + str(ticket_id) + ".json"
        response = requests.post(url, auth=(self.key, "X"), data=data)
        return response.json()
    
    def ticketPutRequest(self, ticket_id, data):
        url = self.url + "/api/v2/tickets/" + str(ticket_id) + ".json"
        response = requests.put(url, auth=(self.key, "X"), data=data)
        return response.json()