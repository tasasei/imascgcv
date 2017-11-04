#!/usr/bin/python3

import json, re, urllib
import requests
import pandas as pd

# 生年 生月 生日
def PearseBirth(key_str,x_str):
    b_year = re.search(('\|\s*' + key_str + '\s*=\s*[0-9]*'),x_str)
    if b_year == None and len(x_str) < 10:
        import pdb; pdb.set_trace()
        return ''
    if b_year == None:
        return '' 
    return re.sub('[^0-9]','',b_year.group(0))

cv_list = pd.read_csv("CVdata.csv",header=None)

for i in cv_list[0]:
# for i in ['伊達朱里紗']:
# x = urllib.parse.urlencode({"titles":"雨宮天"})
# x = urllib.parse.urlencode({"titles":"アイドルマスター_シンデレラガールズ"})
    x = urllib.parse.urlencode({"titles":i})
    url = 'https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&'+x+'&rvprop=content'

    q = requests.get(url)

    page = list(q.json()['query']['pages'].keys())[0]
    honbun_str = q.json()['query']['pages'][page]['revisions'][0]['*']


    b_year = PearseBirth('生年',honbun_str)
    b_mon  = PearseBirth('生月',honbun_str)
    b_day  = PearseBirth('生日',honbun_str)
    birthday_str = b_year + '/' + b_mon + '/' + b_day

    print(birthday_str)
