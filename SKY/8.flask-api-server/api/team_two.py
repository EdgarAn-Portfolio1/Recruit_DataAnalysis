from flask import Blueprint
from flask import jsonify
from flask import make_response
import json

team_two = Blueprint('team_two', __name__)

@team_two.route("/")
def main():
    return "This is Api Service for Team Two"

@team_two.route("/recruit-score")
def recruit_senti_score():
    from modules import news_based_Senti
    news_based_Senti.naver_news_it_recruit("it_recruit_news.csv")
    total_score = news_based_Senti.calculate_score("it_recruit_news.csv", "/Users/sky/class_python/5.Sentiment_Analysis/senti_dict.csv")
    
    return "the senti score is {}".format(str(total_score))
    
@team_two.route("/crawler/jobkorea")
def crawler_jobkorea():
    from modules import recruit_crawler
    recruit_crawler.scrape_jobkorea_recruitIT('recruit1.csv')
    return ('Done')

@team_two.route("/crawler/saramin")
def crawler_saramin():
    from modules import recruit_crawler
    recruit_crawler.scrape_saramin_recruitIT('recruit2.csv')
    return ('Done')

@team_two.route("/crawler/rookie10j")
def rookie_jobkorea():
    from modules import recruit_rookie_hot10_crawler_
    recruit_rookie_hot10_crawler_.scrape_jobkorea_rookie('rookie1.csv')
    return ('Done')

@team_two.route("/crawler/rookie10s")
def rookie_saramin():
    from modules import recruit_rookie_hot10_crawler_
    recruit_rookie_hot10_crawler_.scrape_saramin_rookie('rookie2.csv')
    return ('Done')

@team_two.route('/itemrecommend')
def item_recommend():
    from modules import item_based_recommend
     
    simscores = item_based_recommend.item_based_recommend('/Users/sky/class_python/6.Recommendation/saramin_jobkorea_sjy_real.csv')
    return str(simscores)

@team_two.route('/cfrecommend')
def collaborative_recommend():
    from modules import collaborative_recommend
    predict = collaborative_recommend.collaborative_recommend('/Users/sky/class_python/6.Recommendation/company_member.csv')
    return str(predict)
    


    
    
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

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