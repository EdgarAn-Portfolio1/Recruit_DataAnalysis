def db_jobkorea_saramin():
    import pymysql
    import pandas as pd
    
    
    conn = pymysql.connect(host='localhost',
                        database='shakeit', # 자기 데이터 베이스에 맞게 접속
                        user='root',
                        passwd='mlb10200', #자기 비밀번호
                        charset='utf8',
                        local_infile=1) #혹시나 안되면 이거 켜서 접속

    cursor = conn.cursor()
    
    recruit_info = pd.read_csv('/Users/sky/class_python/2.DB/saramin_jobkorea_sjy_real.csv', index_col=0, encoding='utf8')
    
    value_list = []
    for index, row in recruit_info.iterrows():
        tu = ( row.company, row.duty, row.career, row.degree,  row.work_place,
            row.work_type, row.category, row.link, row.info, row.resource) 
        value_list.append(tu)
        
    cursor.executemany('''
                    INSERT INTO job (company, duty, career, degree, work_place, work_type, category, link, info, resource) 
                    values ( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                    ''', value_list)

    conn.commit()
    conn.close()
    
    print('GOOD!')
    
    
def db_news():
    import pymysql
    import pandas as pd
    
    news = pd.read_csv('/Users/sky/class_python/2.DB/it_news.csv', index_col=0, encoding='utf-8')
    
    conn = pymysql.connect(host='localhost',
                       database='shakeit', # 자기 데이터 베이스에 맞게 접속
                       user='root',
                       passwd='mysql', #자기 비밀번호
                       charset='utf8',
                       local_infile=1) #혹시나 안되면 이거 켜서 접속

    cursor = conn.cursor()

    value_list = []
    for index, row in news.iterrows():
        tu = ( row.title, row.date, row.link, row.content) 
        value_list.append(tu)
        
    cursor.executemany('''
                    INSERT INTO news (title, date, link, content) 
                    values ( %s, %s, %s, %s)
                    ''', value_list)

    conn.commit()
    conn.close()
    
    print("good!")
    
if __name__ == "__main__":
    db_jobkorea_saramin
    db_news