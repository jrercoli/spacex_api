# spacex_api
SpaceX Trello API

Builded with Python 3, Flask microframework and Requests (Apache2 Licensed HTTP lib)

# What does and why?
This is an SpaceX Trello API software application, that allows you to manage the next launch
of the SpaceX team to the ISS.
It was builded with the goal of replace the use of Trello management software for load the tasks 
of the space launch, because the management team wasn't comfortable with its use.
To solve this 3 endpoints were created, one for each task type: Issue, Bug and Task, who have differents
parameters to load.

*An issue*: This represents a business feature that needs implementation, they will provide a short title and a description. All issues gets added to the “To Do” list as unassigned

*A bug*: This represents a problem that needs fixing. They will only provide a description, the title needs to be randomized with the following pattern: bug-{word}-{number}. It doesn't matter that they repeat internally. The bugs should be assigned to a random member of the board and have the “Bug” label.

*A task*: This represents some manual work that needs to be done. It will count with just a title and a category (Maintenance, Research, or Test) each corresponding to a label in trello.

# Trello steps
You should have a Trello account created (https://trello.com/)

Then you must create a simple Board (ex: ToDo, Doing, Done lists) and put the labels names (Bug, Maintenance, Research, Test) in the colour that you want (in 'Show menu' button and 'labels').

Also you have an API Key from here : https://trello.com/app-key and a Token to have you the permission to create the cards in your ToDo list : https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=ServerToken&key={YourAPIKey}

Any doubts with this step go to : https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/task/generate-trello-apikey-token.html

# How to install
Previously you must have Python 3 installed.
1) you must clone this repository in your local machine: git clone ...
2) create a virtual environment with venv (https://docs.python.org/3/library/venv.html) : python3 -m venv /path/to/new/virtual/environment 
3) activate the virtual environment : venv\Scripts\activate
4) install the packages : pip install -r requirements.txt
5) set the FLASK_APP variable : set FLASK_APP=trello_api (windows) - export FLASK_APP=trello_api (linux/ubuntu)
6) launch the flask local server : flask run
7) verify that the service is online, go to your browser and put: http://localhost:5000/about , you receive the message: This is a SpaceX Trello API :)
8) now you need to create a .env file with the content of the example file: trello_env_ex.txt, and put in it the id values of your trello account and board. 
You could find out using some urls of the app that were created for this purpose:
http://localhost:5000/get/boards, http://localhost:5000/get/lists (find the id for your ToDo list), http://localhost:5000/get/labels (find the labels ids), and also put your Trello's ApiKey and Token.

# How to use
Now you could add Cards to your board !!, using your browser or curl.
1) To add an Issue : http://localhost:5000/add_issue/testing/engine 
2) To add a Bug : http://localhost:5000/add_bug/cockpit depressure problem
3) To add a Task : http://localhost:5000/add_task/Clean the rocket
