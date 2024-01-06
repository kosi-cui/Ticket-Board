import pytest
import os
from dotenv import load_dotenv
from src.model.api_agent import APIAgent
load_dotenv("../.env")


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

def test_env():
    api_key = os.getenv('API_KEY')  # Get the value of API_KEY
    helpdesk_url = os.getenv('HELPDESK_URL')  # Get the value of HELPDESK_URL
    assert api_key != None
    assert helpdesk_url != None

def test_agent_ticketGetRequest():
    agent = APIAgent()
    agent.setKey(os.getenv('API_KEY'))
    agent.setUrl(os.getenv('HELPDESK_URL'))
    response = agent.ticketGetRequest(os.getenv('TEST_TICKET_ID'))
    title = response["ticket"]["subject"]
    dash = title.find(" - ")
    title = title[:dash]
    assert title == "Software Troubleshooting"