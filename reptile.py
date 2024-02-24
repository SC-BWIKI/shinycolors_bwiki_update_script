import requests
from bs4 import BeautifulSoup
from card import *
from dic import *
from decode import *
def add_data(data,table):
    for index, row in enumerate(table.find_all('tr')):
        if index < 2:  # 跳过前两行
            continue
        cells = row.find_all(['td', 'th'])  # 获取所有单元格
        if len(cells) >= 5:  # 确保每行至少有5个元素
            # 提取需要的单元格，并指定键名
            row_data = {
                "cardname": word_translate (cells[0].text.strip(),nameDic),
                "get_med": word_translate (cells[3].text.strip(),get_medDic),
                "date": cells[4].text.strip()
            }
        data.append(row_data)

def add_data2(data,table):
    for index, row in enumerate(table.find_all('tr')):
        if index < 2:  # 跳过前两行
            continue
        cells = row.find_all(['td', 'th'])  # 获取所有单元格
        if len(cells) >= 6:  
            row_data = {
                "cardname": word_translate (cells[0].text.strip(),nameDic),
                "get_med": word_translate (cells[3].text.strip(),get_medDic),
                "date": cells[5].text.strip()
            }
        data.append(row_data)

def add_data3(data,table):
    for index, row in enumerate(table.find_all('tr')):
        if index < 2:  # 跳过前两行
            continue
        cells = row.find_all(['td', 'th'])  # 获取所有单元格
        if len(cells) >= 5:  
            row_data = {
                "cardname": word_translate (cells[0].text.strip(),nameDic),
                "get_med": "普通卡池",
                "date": cells[4].text.strip()
            }
        data.append(row_data)


def p_card_reptile():
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    url = 'https://wikiwiki.jp/shinycolors/%E3%83%97%E3%83%AD%E3%83%87%E3%83%A5%E3%83%BC%E3%82%B9%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E4%B8%80%E8%A6%A7'
    # 使用requests获取网页内容
    response = requests.get(url,headers=head)
    webpage = response.text
    # 使用BeautifulSoup解析网页
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.findAll(class_='h-scrollable')
    table2 = soup.findAll(class_='wikiwiki-tablesorter-wrapper')
    table3 = soup.findAll("div",class_='h-scrollable')
    data = []
    for table in [table[2], table[3]]: #卡池SSR、SR
        add_data(data, table)
    add_data2(data,table2[2]) #活动SR
    add_data3(data,table3[5]) #偶像之路卡
    return data

def s_card_reptile():
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    url = 'https://wikiwiki.jp/shinycolors/%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E4%B8%80%E8%A6%A7'
    # 使用requests获取网页内容
    response = requests.get(url,headers=head)
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.findAll(class_='h-scrollable')
    table2 = soup.findAll(class_='wikiwiki-tablesorter-wrapper')
    table3 = soup.findAll("div",class_='h-scrollable')
    #print(table[2])
    data = []
    for table in [table[2],table[4]]: #卡池SSR、SR
        add_data(data, table)
    add_data2(data, table2[3]) #活动SR
    add_data3(data, table3[6]) #283S卡
    #table3[7]为初始持有卡片
    return data