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

# How to install
Previously you must have Python 3 installed.
1) you must clone this repository in your local machine: git clone ...
2) create a virtual environment with venv (https://docs.python.org/3/library/venv.html) : python3 -m venv /path/to/new/virtual/environment 
3) activate the virtual environment : venv\Scripts\activate
4) install the packages : pip install -r requirements.txt
5) set the FLASK_APP variable : set FLASK_APP=sx_trello_api (windows) - export FLASK_APP=sx_trello_api (linux/ubuntu)
6) launch the flask local server : flask run
7) verify that the service is online, go to your browser and put: http://localhost:5000/about , you receive the message: This is a SpaceX Trello API :)

# Trello steps
You should have a Trello account created, if not you go to: https://trello.com/ 
Then you must create a simple Board (ex: ToDo, Doing, Done lists)
Now you need to have the Board id and the ToDo list id. You could find out using some urls of the app that were created for this purpose:
http://localhost:5000/get/boards y http://localhost:5000/get/lists
