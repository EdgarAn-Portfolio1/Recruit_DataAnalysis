def scrape_jobkorea_recruitIT(output_path):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import re
    import time
    import pandas as pd
    
    main_url = 'https://www.jobkorea.co.kr'
    browser = webdriver.Chrome('/Users/sky/Downloads/chromedriver')
    
    job_list_jobkorea = []

    url = 'https://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016#anchorGICnt_{0}'


    for page_num in range(1,2):
        
        browser.get(url.format(page_num))

        soup = BeautifulSoup(browser.page_source, 'html.parser')
        
        
        if soup.select('#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr') == []:
            break
        
        for tag in soup.select('#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr'):
            company = {}

            company['기업명'] = tag.select('td.tplCo > a')[0].text
            company['직무'] = tag.select('td > div > strong > a')[0].text
            
            company['경력'] = tag.select('td.tplTit > div > p.etc > span')[0].text
            company['학력'] = tag.select('td.tplTit > div > p.etc > span')[1].text
            company['근무지'] = tag.select('td.tplTit > div > p.etc > span')[2].text
            company['근무형태'] = tag.select('td.tplTit > div > p.etc > span')[3].text
        
        
            category = []
            for item in tag.select('td.tplTit > div > p.dsc'):
                category.append(item.text)
            company['분류'] = str(category)
            
            detail_url = tag.select_one('td.tplTit > div > strong > a').attrs['href']
            full_detail_url = urljoin(main_url, detail_url)
            company['상세링크'] = full_detail_url
            
            corinfo_url = tag.select_one('td.tplCo > a').attrs['href']
            full_detail_url = urljoin(main_url, detail_url)
            company['기업정보'] = full_detail_url
            
            job_list_jobkorea.append(company)

                
            time.sleep(.5)
                
                
    browser.close()
    
    
    jobkorea = pd.DataFrame(job_list_jobkorea)
    jobkorea.to_csv(output_path, encoding='utf8')
    
    
#################################################################################    
    
def scrape_saramin_recruitIT(output_path):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import re
    import pandas as pd
    
    job_list_python = []
    page_num = 1
    main_url = 'http://www.saramin.co.kr'
    
    while True:
        url = f'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={page_num}&cat_mcls=2&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1#searchTitle'
        req_header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        }
        
        html = requests.get(url, req_header).text
        soup = BeautifulSoup(html, 'html.parser')
        
        if soup.select('div.list_body div.list_item') == []:
            break
        
        for tag in soup.select('div.list_body div.list_item'):
            company_dict = {}
            company_dict["기업명"] = tag.select('div.company_nm a span')[0].text
            company_dict["직무"] = tag.select('div.notification_info a span')[0].text
            company_dict["경력사항"] = tag.select('div.recruit_condition p.career')[0].text
            company_dict["학력"] = tag.select('div.recruit_condition p.education')[0].text
            
            try:    
                company_dict["근무지"] = tag.select('div.company_info p.work_place')[0].text
            except:
                company_dict["근무지"] = ""
                
            try:
                company_dict["근무형태"] = tag.select('div.company_info p.employment_type')[0].text
            except:
                company_dict["근무형태"] = ""

            category_list = []
            
            for item in tag.select('div.notification_info div.job_meta span span'):
                category_list.append(item.text)
            company_dict["분류"] = str(category_list)
            
            detail_url = tag.select_one('div.notification_info a').attrs['href']
            full_detail_url = urljoin(main_url, detail_url)
            company_dict["상세링크"] = full_detail_url
            
            job_list_python.append(company_dict)
            
        page_num += 1
        
        break


    saramin = pd.DataFrame(job_list_python)
    saramin.to_csv(output_path, encoding='utf8')

if __name__ == "__main__":
    scrape_jobkorea_recruitIT('recruit1.csv')
    scrape_saramin_recruitIT('recruit2.csv')
    