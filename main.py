import sys
import os

# Add the src directory of the packaged executable to the Python path
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
sys.path.append(os.path.join(application_path, 'src'))

from src.view.main_view import MainView

if __name__ == "__main__":
    mainView = MainView()
    mainView.runApp()