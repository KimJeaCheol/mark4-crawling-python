from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

# Optional argument, if not specified will search path.
options = Options()
options.headless = True  # 웹 브라우저를 띄우지 않는 headless chrome 옵션
options.add_argument('disable-gpu')    # GPU 사용 안함
options.add_argument('lang=ko_KR')  # 언어 설정

driver = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=options)

driver.get('https://oscar.go.com/winners')
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

category = soup.select(
    'bls-winners-list > ul > li > div.winners-list__info > a'
)
movie = soup.select(
    'bls-winners-list > ul > li > div.winners-list__info > h3 > a'
)
producer = soup.select(
    'bls-winners-list > ul > li > div.winners-list__info > p'
)

oscars_2020 = []
for item in zip(category, movie, producer):
    oscars_2020.append(
        {
            'category': item[0].text,
            'movie': item[1].text,
            'producer': item[2].text
        }
    )

data = pd.DataFrame(oscars_2020)
print(data)
data.to_csv('oscars_2020.csv')

driver.quit()
