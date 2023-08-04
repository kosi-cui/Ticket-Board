from CUI_Client.cui_client import CUI_Client
import eel, os, threading

#region GUI_Setup

def OpenWebsite():
    """
    Opens the website
    """
    eel.init('web')
    eel.start("index.html", close_callback=CloseWebsite)

def CloseWebsite(page, sockets_still_open):
    """
    Closes the website
    """
    print("Closing python backend")
    os._exit(0)

#NOTE: Make sure to add any functions that you want to be able to call from the website to this function
#      -- Naming convention: Eel_<function_name>
def BindEelFunctions(client: CUI_Client):
    """
    Binds the eel functions to the CUI_Client. This is done so that the eel GUI can call specific functions in the CUI_Client
    """
    #NOTE: use eel.expose(client.<function_name>) to expose a function to the website
    #NOTE: To call the function in the website, use eel.<function_name>()
    eel.expose(client.Eel_ExposeTickets)

#endregion

if __name__ == "__main__":
    # Test ticket = 21467
    # Department ID = 19000169805
    fresh = CUI_Client()
    gui_thread = threading.Thread(target=OpenWebsite)
    gui_thread.start()
    BindEelFunctions(fresh)

    while True:
        continue

    gui_thread.join()