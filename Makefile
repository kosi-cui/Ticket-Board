VENV_NAME?=.venv
SCRIPT_FOLDER?=bin
PYTHON=$(VENV_NAME)\$(SCRIPT_FOLDER)\python

setup: $(VENV_NAME)\$(SCRIPT_FOLDER)\activate
	echo "To activate your venv, run: .\$(VENV_NAME)\$(SCRIPT_FOLDER)\activate"

$(VENV_NAME)\$(SCRIPT_FOLDER)\activate: requirements.txt
	if not exist $(VENV_NAME) (python -m venv $(VENV_NAME))
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements.txt

dist:
	if exist "build" (rmdir /s /q build)
	if not exist "build" (mkdir build)
	$(PYTHON) -m PyInstaller --onefile --distpath build src/gui.py