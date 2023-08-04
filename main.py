from CUI_Client.cui_client import CUI_Client

if __name__ == "__main__":
    # Test ticket = 21467
    # Department ID = 19000169805
    fresh = CUI_Client()
    fresh.SaveReimages()
    while True:
        continue