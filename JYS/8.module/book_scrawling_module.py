def scrape_it_book(output_path):
    import requests
    from bs4 import BeautifulSoup
    import time
    import pandas as pd

    book_ITbestseller =[]

    url = 'http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb=KOR&linkClass=33&menuCode=002'
    # browser.get(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for tag in soup.select('#frmList > ul > li > div > div > .detail'):

        if soup.select('#frmList > ul > li > div > div > .detail') == []:
            break
        book = {}

        book['book_name'] = tag.select('div > a')[0].text
        f = tag.select_one('div > a')['href'].find('(')
        t = tag.select_one('div > a')['href'].find(')')

        d = tag.select_one('div > a')['href'][f+1:t]
        dr = d.replace("\'", "").split(",")

        lnk = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb={0}&ejkGb={0}&linkClass={1}&barcode={2}'.format(dr[0].strip(), dr[1].strip(), dr[2].strip())
        book['link'] = lnk

        book['writer'] = tag.select('.pub_info > span')[0].text
        # book['출판사'] = tag.select('.pub_info > span')[1].text
        # book['초판일'] = tag.select('.pub_info > span')[2].text
        book['price'] = tag.select('.price > strong')[0].text
        # book['할인율'] = tag.select('.price > span')[0].text
        book['grade'] = tag.select('.review_score > span > strong')[0].text

        book_ITbestseller.append(book)

    book_IT_bestseller = pd.DataFrame(book_ITbestseller)

    book_IT_bestseller['grade'] = book_IT_bestseller['grade'].str.replace('\t','')
    book_IT_bestseller['grade'] = book_IT_bestseller['grade'].str.replace('\r\n','')
    book_IT_bestseller['grade'] = book_IT_bestseller['grade'].str.replace(' ','')

    book_IT_bestseller.reset_index(inplace=True)

    book_IT_bestseller = book_IT_bestseller.rename(columns={'index':'number'})

    book_IT_bestseller['number'] = book_IT_bestseller['number'] +1
    
    book_IT_bestseller.to_csv(output_path,encoding='utf8')

if __name__ == "__main__":
    scrape_it_book