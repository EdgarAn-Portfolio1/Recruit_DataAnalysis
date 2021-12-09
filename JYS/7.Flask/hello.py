from flask import Flask
from flask import jsonify
from flask import make_response
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "This is Flask Web Application"

@app.route("/hello")
def hello():
    return "<h2 style='text-align:center'>Hello, Flask Web</h2>"

@app.route("/api/person/<int:id>")
def person(id):
    p = {}
    if id==1:
        p["name"] = "John Doe"
        p["email"] = "johndoe@example.com"
        p["phone"] = "010-9876-5432"
        p["birth"] = '1995-12-07'
    else:
        p = {
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "phone": "010-2345-6789",
            "birth": '1997-11-03'
        }

    return p

@app.route("/api/persons")
def persons():
    result = jsonify([{
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "010-9876-5432",
        "birth": '1995-12-07'
    }, {
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "phone": "010-2345-6789",
        "birth": '1997-11-03'
    }])

    return result

@app.route("/api/persons2")
def persons2():
    result = json.dumps([{
        "name": "장동건",
        "email": "hkd@example.com",
        "phone": "010-9876-5432",
        "birth": '1995-12-07'
    }, {
        "name": "김윤석",
        "email": "janedoe@example.com",
        "phone": "010-2345-6789",
        "birth": '1997-11-03'
    }], ensure_ascii=False, indent=4)

    response = make_response(result)
    response.content_type = "application/json;charset=utf-8"

    return response