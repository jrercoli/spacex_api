from flask import Flask, request
import requests
import os
import random
from dotenv import load_dotenv

# Trello ids
load_dotenv()
TRELLO_KEY = os.getenv('TRELLO_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
TRELLO_BOARD = os.getenv('TRELLO_BOARD')
TRELLO_TODO_LIST = os.getenv('TRELLO_TODO_LIST')
TRELLO_MEMBER_ID = os.getenv('TRELLO_MEMBER_ID')
TRELLO_MEMBER_NAME = os.getenv('TRELLO_MEMBER_NAME')
TRELLO_LBL_BUG = os.getenv('TRELLO_LBL_BUG')
TRELLO_LBL_RSCH = os.getenv('TRELLO_LBL_RSCH')
TRELLO_LBL_MAINT = os.getenv('TRELLO_LBL_MANT')
TRELLO_LBL_TEST = os.getenv('TRELLO_LBL_TEST')
# create labels dict
task_lbls = {'maint': TRELLO_LBL_MAINT, 'rsch': TRELLO_LBL_RSCH, 'test': TRELLO_LBL_TEST}

app = Flask(__name__)

@app.route('/about')
def about():
    return 'This is SpaceX API Trello'

@app.route('/get/boards', methods=['GET'])
def boards():
    """
    Purpose:
        Return member id and board id to put in Trello env.
    Args:
        N/A
    """
    url = "https://api.trello.com/1/members/me/boards"
    payloads = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN}
    r = requests.get(url, params=payloads)
    data = r.json()
    member_id = data[0]['idMemberCreator']
    board_id = data[0]['id']
    return 'MemberId: ' + member_id + '  BoardId: ' + board_id

@app.route('/get/lists', methods=['GET'])
def lists():
    """
    Purpose:
        Return trello lists to found To Do list id and put in Trello env.
    Args:
        N/A
    """
    url = "https://api.trello.com/1/boards/" + TRELLO_BOARD + "/lists"
    payloads = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN}
    r = requests.get(url, params=payloads)
    return r.text

@app.route('/get/labels', methods=['GET'])
def labels():
    """
    Purpose:
        Return labels ids to put in Trello env.
    Args:
        N/A
    """
    url = "https://api.trello.com/1/boards/" + TRELLO_BOARD + "/labels"
    payloads = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN}
    r = requests.get(url, params=payloads)
    return r.text

@app.route('/add_issue/<title>/<description>', methods=['GET', 'POST'])
def add_issue(title, description):
    """
    Purpose:
        Add Issue task to the board in To Do list
    Args:
        title (string)
        description (string)
    """
    url = "https://api.trello.com/1/cards"
    payloads = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN, 'idList': TRELLO_TODO_LIST,
                'name': title, 'desc': description}
    r = requests.request("POST", url, params=payloads)
    return r.text

@app.route('/add_bug/<description>', methods=['GET', 'POST'])
def add_bug(description):
    """
    Purpose:
        Add Bug task to the board in To Do list
    Args:
        description (string)
    """
    title = create_bug_title()
    idMembers = [TRELLO_MEMBER_ID]
    url = "https://api.trello.com/1/cards"
    payloads = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN, 'idList': TRELLO_TODO_LIST,
                'name': title, 'desc': description, 'idLabels': TRELLO_LBL_BUG, 'idMembers': idMembers}
    r = requests.request("POST", url, params=payloads)
    return r.text

@app.route('/add_task/<title>', methods=['GET', 'POST'])
def add_task(title):
    """
    Purpose:
        Add Task to the board in To Do list
    Args:
        title (string)
    """
    # Create random label category
    idLabels=[]
    idLabels.append(random.choice(list(task_lbls.values())))

    url = "https://api.trello.com/1/cards"
    payloads = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN, 'idList': TRELLO_TODO_LIST,
                'name': title, 'idLabels': idLabels}
    r = requests.request("POST", url, params=payloads)
    return r.text

def create_bug_title():
    words = ['A', 'B', 'C', 'D', 'E']
    word = random.choice(words)
    number = random.randint(1000, 9999)
    return 'bug-' + word + '-' + str(number)