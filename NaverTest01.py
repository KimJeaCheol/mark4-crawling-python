import requests as rq
import json
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/%EB%84%A4%EC%9D%B4%EB%B2%84%20%EC%98%88%EC%95%BD%20%ED%8C%8C%ED%8A%B8%EB%84%88%EC%84%BC%ED%84%B0%20%EA%B0%84%EB%8B%A8%EC%98%88%EC%95%BD%EA%B4%80%EB%A6%AC.html"

res = rq.get(url)

# print(res)
# print(res.status_code)
# print(res.encoding)
# print(res.content)

soup = BeautifulSoup(res.content, 'lxml')
# print(soup.body)

htmlbody = soup.body

# print(htmlbody.children)
# print(htmlbody.previous_sibling)

# print(htmlbody.get('class'))
htmltable = htmlbody.find_all('table', {"class": "table"})


def dataParser(tr_list):
    print(tr_list[0])
    print(tr_list[1])

# 재귀함수를 사용하세요.


def bangBlock(tbodylist):
    print(tbodylist.select('tr')[0])


tbodycount = 0
listinfo = []

# 예약한 날짜로 인덱스 구하기


def searchDate(dateinfo):
    dateindex = 3
    thtag = htmlbody.select('table thead tr th')
    while dateindex < len(thtag):
        if thtag[dateindex].text == dateinfo:
            break
        dateindex += 1

    print(thtag[dateindex].string)
    return dateindex

# 예약한 방정보로 인덱스 구하기


def searchRoom(roominfo):
    roomindex = 0
    tbodytag = htmlbody.select('table tbody')
    while roomindex < len(tbodytag):
        trtag = tbodytag[roomindex].select('tr')
        if trtag[0].find('th').string == roominfo:
            break
        roomindex += 1

    print(tbodytag[roomindex].select('tr')[0].find('th').string)

    roomcheck = False

    if roomcheck != tbodytag[roomindex].select('tr')[0].find(
            'td').find('input', checked=True):
        roomcheck = True

    return roomindex, roomcheck

# 예약날짜에 방을 확인하고 방을막는다.


def roomdateCheck(roomindex, dateindex):
    roomdateCheck = False
    if roomdateCheck != htmlbody.select('table tbody')[roomindex].select(
            'tr')[0].select('td')[dateindex - 1].find('input', checked=True):
        roomdateCheck = True

    return roomdateCheck


# 문자메세지 정보로 예약방 막기
dateindex = searchDate("4월 3일(금)")
roomindex, roomcheck = searchRoom("201호(스파)")
print(str(roomindex) + '||' + str(dateindex))
print(roomcheck)
roomdateCheck = roomdateCheck(roomindex, dateindex)
print(roomdateCheck)
btnClick = '//*[@id = "content"]/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody[{}]/tr[1]/td[{}]/div/div/input'.format(
    str(roomindex + 1), str(dateindex))
print(btnClick)


# for tbodyTag in soup.select('body table tbody'):
#     bangBlock(tbodyTag.select('tr')[0])  # 상품명,상품노출,판매여부,스위치
#     bangBlock(tbodyTag.select('tr')[1])  # 그룹, 그룹, 확정/전체, 숫자
#     tbodycount += 1

# print(tbodycount)

# print(htmltable.children)
# table = soup.find('table').find_all(
#     "tbody", {"class": "switch-body"})

# print(table)
