def scrape_saramin_rookie(output_path):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time
    import pandas as pd
    
    browser = webdriver.Chrome('/Users/sky/Downloads/chromedriver')
    
    url = 'https://www.saramin.co.kr/zf_user/jobs/hot100'
    browser.get(url)    
    
    browser.find_element_by_xpath('//*[@id="search_panel_wrapper"]/form/fieldset/div/div[1]/div/div/button[7]').click()
    time.sleep(1)
    
    soup = BeautifulSoup(browser.page_source)
    
    browser.close()
    
    rank_rookie = []

    for tag in soup.select('#content > div.recruit_hot_wrap > div.recruit_hot_list > div.careers > div > ul > li'):
        company = {}    
        #company['rank'] = tag.select('div.area_rank > div.rank_info > .rank_num')[0].text
        company['company'] = tag.select('div.area_rank > div.rank_company_info > a > span')[0].text
        company['title'] = tag.select('div.area_detail > a.tit > span')[0].text
        
        company['career'] = tag.select('div.area_detail > div > span')[0].text
        company['degree'] = tag.select('div.area_detail > div > span')[1].text
        company['work_type'] = tag.select('div.area_detail > div > span')[2].text
        
        try:
            company['work_place'] = tag.select('div.area_detail > div > span')[3].text
        except:
            company['work_place'] = ""

        company['duty'] = tag.select('.area_detail > ul')[0].text
        company['due_date'] = tag.select('div.area_detail > dl > dd')[0].text
        
        rank_rookie.append(company)
        
    df = pd.DataFrame(rank_rookie)
    
    df = df.replace('\n', '', regex=True)
    
    df.to_csv(output_path, encoding='utf8')
    
    
    
def scrape_jobkorea_rookie(output_path):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time
    import pandas as pd
    
    url = 'https://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10016&BizJobtype_Bctgr_Name=IT·인터넷&BizJobtype_Code=0&BizJobtype_Name=IT·인터넷+전체&Major_Big_Code=0&Major_Big_Name=전체&Major_Code=0&Major_Name=전체&Edu_Level_Code=9&Edu_Level_Name=전체&Edu_Level_Name=전체&MidScroll=0'
    browser = webdriver.Chrome('/Users/sky/Downloads/chromedriver')
    browser.get(url)
    
    soup = BeautifulSoup(browser.page_source)
    
    rank_rookie = []

    for tag in soup.select('#devTypeTab_1 > div.rankListWrap > div.rankListArea.devSarterTab > ol > li '):
        company = {}    
        company['rank'] = tag.select('div > span.num')[0].text
        company['company'] = tag.select('div.co > div.coTit > a')[0].text
        company['title'] = tag.select('div.info > div.tit')[0].text
        company['duty'] = tag.select('div.info > div.sTit')[0].text
        company['career'] = tag.select('div.info > div.sDsc > span')[0].text
        company['degree'] = tag.select('div.info > div.sDsc > span')[1].text
        company['work_place'] = tag.select('div.info > div.sDsc > span')[2].text
        company['work_type'] = tag.select('div.info > div.sDsc > span')[3].text

        company['due_date'] = tag.select('div.side > span.day')[0].text
        
        rank_rookie.append(company)
        
    df = pd.DataFrame(rank_rookie)
    
    df = df.replace('\n', '', regex=True)
    
    df.to_csv(output_path, encoding='utf8')
    

    
    
    
if __name__ == "__main__":
    scrape_saramin_rookie('test1.csv')
    scrape_jobkorea_rookie('test2.csv')