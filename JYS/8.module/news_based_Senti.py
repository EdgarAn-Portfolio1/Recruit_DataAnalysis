def naver_news_it_recruit(output_path):
    import os
    import sys
    import urllib.request
    import pandas as pd
    import json
    import re
    
    import pandas as pd
    from konlpy.tag import Okt
    from nltk import WhitespaceTokenizer
    from collections import Counter
    
    client_id = "mNhJ01jj6_6mlvwLR3uy" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "JAHWSRUs2D" # 개발자센터에서 발급받은 Client Secret 값
    
    query = urllib.parse.quote(input("궁금한 주제가 머꼬: "))
    
    #encText = urllib.parse.quote('취업 "it"')
    idx = 0
    display = 100
    start = 1
    end = 1000

    web_df = pd.DataFrame(columns=('title', 'link', 'description', 'pubDate'))

    for start_index in range(start, end, display): # 1 ~ 1000까지 100개씩 가지고 올끼야
        

        url = "https://openapi.naver.com/v1/search/news.json?query=" + query \
                +'&display=' + str(display) \
                +'&sort=date' \
                +'&start=' + str(start_index)
                
        request = urllib.request.Request(url)

        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)

        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            response_dict = json.loads(response_body.decode('utf-8'))
            items = response_dict['items'] 
            
            for item_index in range(0, len(items)):
                remove_tag = re.compile('<.*?>')
                title = re.sub(remove_tag, '', items[item_index]['title'])
                link = items[item_index]['link']
                description = re.sub(remove_tag, '', items[item_index]['description'])
                pubDate = items[item_index]['pubDate']
                
                web_df.loc[idx] = [title, link, description, pubDate]
                idx += 1
                
        else: print("Error Code:" + rescode)
        
    
    web_df["title_description"] = web_df["title"] + " " + web_df["description"]
    
    web_df.to_csv(output_path, encoding="utf8")
    
    
    content = web_df['title_description']
    
    df2 = pd.read_csv('/Users/sky/class_python/5.Sentiment_Analysis/senti_dict.csv', index_col=0)
    df2
    
    e_dict = df2.reset_index()
    e_dict2 = { w : s for w, s in e_dict.values }
    
    total_score2 = 0
    for sentence in web_df["title_description"].values:
        total_score = 0
        for word in sentence.split(" "):
            try:
                score = e_dict2[word]
            except:
                score = 0
            total_score += score
        total_score2 += total_score
        #print(total_score)
        
    print(total_score2)
    
if __name__ == "__main__":
    naver_news_it_recruit('news_it_recruit_naver.csv')