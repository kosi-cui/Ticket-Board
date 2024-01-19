import pytest
import os
from dotenv import load_dotenv
from src.model.config import Config
load_dotenv("../.env")
# This loads the following env variables:
# API_KEY
# HELPDESK_URL
# TEST_TICKET_ID

#region Init & Setter Tests
def test_config_init():
    config = Config()
    assert config.title == "ReimageBoard"
    assert config.geometry == "400x240"
    assert config.bg_color == "white"


def test_confg_login():
    config = Config()
    assert config.logIn(os.getenv('API_KEY'), os.getenv('HELPDESK_URL')) == True
    assert config.api_agent.valid_user == True
    assert config.api_agent.key == os.getenv('API_KEY')
    assert config.api_agent.url == os.getenv('HELPDESK_URL')


def test_config_change_api_user():
    config = Config()
    assert config.logIn("123456", os.getenv('HELPDESK_URL')) == False
    assert config.changeAPIUser(os.getenv('API_KEY')) == True

def test_config_change_api_url():
    config = Config()
    assert config.logIn(os.getenv('API_KEY'), "https://google.com") == False
    assert config.changeAPIUrl(os.getenv('HELPDESK_URL')) == True
#endregion



#region Getter Tests
def test_getCurrentTicket():
    config = Config()
    config.logIn(os.getenv('API_KEY'), os.getenv('HELPDESK_URL'))
    assert config.getCurrentTicket() == None
    config.api_agent.getTicket(os.getenv('TEST_TICKET_ID'))
    ticket = config.getCurrentTicket()
    assert ticket != None
    assert config.getCurrentTicket() != None


#endregion
