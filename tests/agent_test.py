import pytest
import os
from dotenv import load_dotenv
from src.model.api_agent import APIAgent
load_dotenv("../.env")


#region Init & Setter Tests
def test_agent_init():
    agent = APIAgent()
    assert agent.key == None
    assert agent.url == None

def test_agent_setters():
    agent = APIAgent()
    agent.setKey("123456789")
    agent.setUrl("https://test.freshservice.com")
    assert agent.key == "123456789"
    assert agent.url == "https://test.freshservice.com"

def test_valid_key():
    agent = APIAgent(url=os.getenv('HELPDESK_URL'))
    agent.setKey("123456789")
    assert agent.validKey() == False
    agent.setKey(os.getenv('API_KEY'))
    assert agent.validKey() == True
#endregion
    


#region Local Environment Variable Tests -- Allows tests below to run properly
def test_env_load():
    api_key = os.getenv('API_KEY')  # Get the value of API_KEY
    helpdesk_url = os.getenv('HELPDESK_URL')  # Get the value of HELPDESK_URL
    assert api_key != None
    assert helpdesk_url != None
#endregion



#region API Call Tests
def test_valid_ticketGetRequest():
    agent = APIAgent(os.getenv('API_KEY'), os.getenv('HELPDESK_URL'))
    response = agent.ticketGetRequest(os.getenv('TEST_TICKET_ID'))
    title = response["ticket"]["subject"]
    dash = title.find(" - ")
    title = title[:dash]
    assert title == "Reimage"

def test_unauth_ticketGetRequest():
    agent = APIAgent()
    agent.setKey("123456")
    agent.setUrl(os.getenv('HELPDESK_URL'))
    response = agent.ticketGetRequest("123456789")
    assert response == None

def test_nonexistent_ticketGetRequest():
    agent = APIAgent(os.getenv('API_KEY'), os.getenv('HELPDESK_URL'))
    response = agent.ticketGetRequest("123456789")
    is_error = "error" in response
    assert is_error == True

def test_valid_filteredTicketGetRequest():
    agent = APIAgent(os.getenv('API_KEY'), os.getenv('HELPDESK_URL'))
    response = agent.filteredTicketGetRequest("tag:Reimage")
    filter_exists = "error" not in response
    assert filter_exists == True
#endregion



#region Parsing Tests
def test_valid_getTicketTitle():
    agent = APIAgent(os.getenv('API_KEY'), os.getenv('HELPDESK_URL'))
    _ = agent.ticketGetRequest(os.getenv('TEST_TICKET_ID'))
    title = agent.getTicketTitle()
    dash = title.find(" - ")
    assert title[:dash] == "Reimage"

def test_invalid_getTicketTitle():
    agent = APIAgent(os.getenv('API_KEY'), os.getenv('HELPDESK_URL'))
    title = agent.getTicketTitle()
    assert title == None
#endregion