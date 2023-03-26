from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import pandas as pd
import re
from bs4 import BeautifulSoup

def html_code(url):
    # pass the url into getdata function
    soup = BeautifulSoup(url, 'html.parser')
  
    # display html code
    return (soup)


options = Options()
# Enable Headless
# options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

# Get the Link
driver.get("https://www.tokopedia.com/caseayangan-id/pocket-anticrack-card-case-iphone-6-7-plus-8-x-xr-11-12-13-14-pro-max-iphone-6-6s/review")

last_page = int(driver.find_element(By.CSS_SELECTOR, '.css-1ni9y5x-unf-pagination-items > li:nth-child(10) > button:nth-child(1)').text)

name = []
review = []
bintang = []
terbantu = []
kendala = []

for page in range(last_page) :

    from time import sleep
    sleep(1)

    # Biar reviewnya keliatan semua (lihat selengkapnya)
    for i in range(11) :
        try :
            driver.find_element(By.CSS_SELECTOR, f'article.css-1cvpirb:nth-child({i}) > div:nth-child(1) > p:nth-child(4) > button:nth-child(2)').click()
        except :
            pass
    
    soup = html_code(driver.find_element(By.CSS_SELECTOR, '.css-1799hu').get_attribute('innerHTML'))

    for item in soup.findAll("span", class_ ="name"):
        name.append(item.get_text())

    for item in soup.findAll("span", class_ ="css-q2y3yl"):
        terbantu.append(item.get_text())
    
    # for item in soup.findAll("p", class_ ="css-1u4eofn-unf-heading e1qvo2ff8"):
    #     try : 
    #         if item.get_text() == '\n' :
    #             review.append('gada')
    #             pass
    #         else :
    #             review.append(item.get_text())
    #     except :
    #         pass
    #         review.append('gada')

    for i in range(1,int(driver.find_element(By.CSS_SELECTOR, '.css-13b4yo8-unf-heading').text [12 : 14]) + 1):
        try:
            review.append(driver.find_element(By.CSS_SELECTOR, f'article.css-1cvpirb:nth-child({i}) > div:nth-child(1) > p:nth-child(4) > span:nth-child(1)').text)
        except :
            try :
                review.append(driver.find_element(By.CSS_SELECTOR, f'article.css-1cvpirb:nth-child({i}) > div:nth-child(1) > p:nth-child(3) > span:nth-child(1)').text)
            except :
                review.append('gada')
        try : 
            kendala.append(driver.find_element(By.XPATH, f'//*[@id="review-feed"]/article[{i}]/div/p[3]').text)
        except :
            kendala.append('gada')

    for i in range(1,11):
        try:
            bintang.append(driver.find_element(By.CSS_SELECTOR, f'article.css-1cvpirb:nth-child({i}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').get_attribute('aria-label')[8])
        except :
            pass

    # Wait until the next review button is clickable
    if (page == last_page - 1) : break
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-1ni9y5x-unf-pagination-items > li:nth-child(11) > button:nth-child(1)'))).click()

problem = [k.replace('Kendala:', '') for k in kendala]
helpful = [0 if t == 'Membantu' else int(re.search(r'\d+', t).group()) for t in terbantu]

data = {'Name' : name,
        'Review' : review,
        'Star' : bintang,
        'Helpful' : helpful,
        'Problem' : problem}

df = pd.DataFrame(data)

df.to_csv('Tokped_review.csv', index=False)