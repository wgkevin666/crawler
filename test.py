#! /usr/local/bin/python3.8
import requests
import re
import json
from bs4 import BeautifulSoup

# Get Topic
url = 'https://www.dcard.tw/f/money'
reps = requests.get(url)
# print(reqs)
# print(reqs.text)
item = reps.text
items = BeautifulSoup(reps.text, 'html.parser')
# print(items)
datas = items.find_all("article" ,attrs={"class":"sc-1v1d5rx-0 lmtfq"})
data_topic = []

for link in datas:
    h2_tags = link.find("h2", attrs={"class":"sc-1v1d5rx-2 kZjhSU"})
    partial_link = h2_tags.find("span").text.strip()
    data_topic.append(partial_link)
#print(data_topic)

# Get Link
mainurl = 'https://www.dcard.tw'
url = 'https://www.dcard.tw/f/money'
reps = requests.get(url)
# print(reps)
# print(reqs.text)
item = reps.text
items = BeautifulSoup(reps.text, 'html.parser')
#print(items)
datas = items.find_all("article" ,attrs={"class":"sc-1v1d5rx-0 lmtfq"})
data_list = []


for link in datas:
    h2_tags = link.find("h2", attrs={"class":"sc-1v1d5rx-2 kZjhSU"})
    partial_link = h2_tags.find("a").get("href")
    data_list.append(partial_link)

url_list = [ mainurl + data_list[i] for i in range(len(data_list))]
#print(url_list)  
#print(data_list)
dictionary = dict(zip(data_topic, url_list))
#print(dictionary)
print(json.dumps(dictionary))
