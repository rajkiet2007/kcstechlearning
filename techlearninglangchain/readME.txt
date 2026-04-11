Step -1 Download the Python Latest stable version from the Web
Step -2 - Install the Python Latest version.
Step-3 - Download the VS code latest version.
Step-4 -  Install the VS code.
Step-5 Create a folder of your project on Drive- D:\AITech
Step-6 - Create the Virtual env in the project folder -
	python -m venv venv
Step - 7 - Install the Python Extension in the VS Code.
Step -8 ctrl+shit+P - Select python interpreter
	Select the Browse option. Browse the venv/Script/python.exe folder project folder
Step- 9- install the dependency by the command
	  pip install dependency_name
Step - 10 create a .vscode folder in the root folder of the project
	Create the Launch.json and create the configuration like below
	{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Run Modular App",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/app.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src"
            }
        }
    ]
}
Step -11- create .env file for getting Environment variable on root folder

Step -12 - Freeze the requirements.txt
           pip freeze > requirements.txt

Step - 13 for the re-run the project on other environment
        install the requirements.txt
	pip install -r requirements.txt

	
