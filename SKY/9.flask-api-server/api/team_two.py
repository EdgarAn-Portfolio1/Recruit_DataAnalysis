from flask import Blueprint
from flask import jsonify
from flask import make_response
import json

team_two = Blueprint('team_two', __name__)

# @team_two.route("/")
# def index():
#     return "This is Api Service for Team Two"

@team_two.route("/recruit-score")
def index():
    from modules import news_based_Senti
    news_based_Senti.naver_news_it_recruit("it_recruit_news.csv")
    total_score = news_based_Senti.calculate_score("it_recruit_news.csv", "/Users/sky/class_python/5.Sentiment_Analysis/senti_dict.csv")
    return str(total_score)

@team_two.route("/demo-one")
def demo_one() :
    return {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "010-9438-4907",
        "birth": "1990-07-23"
    }

@team_two.route("/demo-two")
def demo_two() :
    return jsonify([{
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "010-9438-4907",
        "birth": "1990-07-23"
    }, {
        "name": "홍길동",
        "email": "hkd@example.com",
        "phone": "010-8687-2399",
        "birth": "1990-04-21"
    }])

@team_two.route("/demo-three")
def demo_three() :
    response = make_response(json.dumps([{
                "name": "John Doe",
                "email": "johndoe@example.com",
                "phone": "010-9438-4907",
                "birth": "1990-07-23"
            }, {
                "name": "홍길동",
                "email": "hkd@example.com",
                "phone": "010-8687-2399",
                "birth": "1990-04-21"
            }], ensure_ascii=False, indent=4))
    response.content_type = "application/json;charset=utf-8"

    return response