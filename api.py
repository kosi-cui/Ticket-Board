import requests, os, json

API_KEY = -1
URL = -1
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = os.path.join(os.sep, CURR_DIR, ".credentials", "conf")


def InitialSetup():
    if not os.path.exists(os.path.join(os.sep, CURR_DIR, ".credentials")):
        os.mkdir(os.path.join(os.sep, CURR_DIR, ".credentials"))

    if not os.path.exists(CONFIG_PATH):
        print("Please enter your FreshService API key: ")
        key = input()
        print("Please enter the base FreshService URL (e.g. https://helpdesk.freshservice.com): ")
        url = input()
        with open(CONFIG_PATH, 'w') as f:
            f.write(f"Key: {key}\n")
            f.write(f"URL: {url}/api/v2/tickets/\n")
        print("Login info saved to " + CONFIG_PATH)
    ReadConfig()


def ReadConfig():
    global API_KEY, URL, API_OBJ
    with open(CONFIG_PATH, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "Key" in line:
                API_KEY = line.split(" ")[1].strip('\n')
            if "URL" in line:
                URL = line.split(" ")[1].strip('\n')

    if(API_KEY == -1):
        print("Error: API key not found in config file")
        exit(1)
    if(URL == -1):
        print("Error: URL not found in config file")
        exit(1)



def GetTicketInfo(ticket_id, args = []):
    # Create the URL for the specified ticket + args

    # The responder_id is the person who currently has the ticket.
    # TODO: Add a way to get the name of the responder_id
    url = URL + str(ticket_id)
    if(len(args) > 0):
        url +="?include="
        for arg in args:
            url += arg

    # Get the ticket info
    response = requests.get(url, auth = (API_KEY, "X"))
    return response


def GetTicketTasks(ticket_id):
    # Status 3 == Closed, Status 1 == Unresolved
    url = URL + str(ticket_id) + "/tasks"
    response = requests.get(url, auth = (API_KEY, "X"))
    return response



if __name__ == "__main__":
    InitialSetup()
    t = GetTicketTasks(21467)
    with open ("testTasks.json", 'w') as f:
        json.dump(t.json(), f, indent = 4)
    t = GetTicketInfo(21467)
    with open ("testTicket.json", 'w') as f:
        json.dump(t.json(), f, indent = 4)