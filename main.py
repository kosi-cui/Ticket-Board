from CUI_Client.cui_client import CUI_Client
import eel, os, threading

#region GUI_Setup


def CloseWebsite(page, sockets_still_open):
    """
    Closes the website
    """
    print("[PY] Closing python backend")
    os._exit(0)


def BindEelFunctions(eel_functions):
    """
    Binds the eel functions to the CUI_Client. This is done so that the eel GUI can call specific functions in the CUI_Client
    """
    #NOTE: To call the function in the website, use eel.<function_name>()
    for function in eel_functions:
        print(f"[PY] Exposing {function.__name__} -> ./web/eel.js")
        eel.expose(function)
    print(f"[PY] Exposed {len(eel_functions)} functions to the website")


#endregion

if __name__ == "__main__":
    # Test ticket = 21467
    # Department ID = 19000169805
    fresh = CUI_Client()
    eel.init('web')
    #gui_thread = threading.Thread(target=OpenWebsite)
    #gui_thread.start()

    #NOTE: Add all functions that need to be exposed to the website here
    eel_functions = [
        fresh.Eel_ExposeTickets,
        fresh.Eel_Print
    ]
    BindEelFunctions(eel_functions)
    

    print("[PY] Opening website")
    eel.start("index.html", close_callback=CloseWebsite)
    while True:
        eel.sleep(.5)