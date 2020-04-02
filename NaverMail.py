from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # 태그가 없는 예외 처리
from bs4 import BeautifulSoup
import time
import random
from myconfig import NAVER
import pyperclip


def load_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
    # options.add_argument('disable-gpu')    # GPU 사용 안함
    # options.add_argument('lang=ko_KR')  # 언어 설정

    driver = webdriver.Chrome(
        executable_path="./chromedriver.exe", options=options)
    return driver


def load_login_page():
    driver.implicitly_wait(3)
    driver.get("https://nid.naver.com/nidlogin.login")


def try_login():
    tag_id = driver.find_element_by_name('id')
    tag_id.click()
    pyperclip.copy(myId)
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    # for id in myId:
    #     time.sleep(0.03)
    #     driver.find_element_by_name('id').send_keys(id)

    # for pw in myPss:
    #     time.sleep(0.04)
    #     driver.find_element_by_name('pw').send_keys(pw)
    tag_pw = driver.find_element_by_name('pw')
    tag_pw.click()
    pyperclip.copy(myPss)
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # driver.find_element_by_xpath(
    #     '//*[@id = "log.login"]').click()
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    time.sleep(3)


def get_maillist_from_mailbox():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    titles = BeautifulSoup.findAll('table', attrs={'class': 'table'})
    for title in titles:
        print(title.text)

# 등록된 펜션 상세정보


def move_to_mailbox():
    # https: // easybooking.naver.com/service/252276/status/resocStockManage
    driver.find_element_by_xpath('//*[@id="0_fol"]/span/a[1]').click()
    time.sleep(3)

# 등록된 펜션 리스트


def request_webpage(url):
    driver.get(url)


def naver_stuff():
    load_login_page()
    try_login()
    request_webpage(
        "https://easybooking.naver.com/service/252276/status/resocStockManage")
    # driver.find_element_by_xpath('//*[@id = "content"]/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody[{}]/tr[1]/td[{}]/div/div/input'.format(
    #     str(roomindex + 1), str(dateindex))).click()
    # move_to_mailbox()
    # get_maillist_from_mailbox()


def prevent_close():
    user_choice = input("Press [ENTER] TO terminate")
    if not user_choice:
        print("terminated...")
        quit()


myId = NAVER["id"]
myPss = NAVER["password"]

if __name__ == "__main__":
    driver = load_driver()
    naver_stuff()
    prevent_close()
