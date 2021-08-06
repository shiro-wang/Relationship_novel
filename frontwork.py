import requests
from bs4 import BeautifulSoup
import json

url = "https://zh.wikipedia.org/wiki/%E7%A5%9E%E9%B5%B0%E4%BF%A0%E4%BE%B6"
#只有首次點選才會post cookie
r = requests.session()
response = r.get(url)
soup = BeautifulSoup(response.text,"html.parser")
original_page = soup
#article_num = 1
#開始找
with open('C://Users//user//Desktop//Python//hw3//characters.txt', 'w' , encoding='utf-8') as character_file:
    table = soup.find_all("td",{"style":"text-align:left;"})
    for t in table:
        if(t.find("a")):
            test=t.find("a").string
            print(test)
            character_file.write(test+"\n")
