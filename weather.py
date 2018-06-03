# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:40:37 2018

@author: th
"""

import urllib.request as r
import json
from xpinyin import Pinyin
pin = Pinyin()
city=input("欢迎使用天气查询系统，请输入城市：")
city_1 = pin.get_pinyin(city,"")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(url.format(city_1)).read().decode('utf-8','ignore')
data=json.loads(info)
print("今日天气情况如下：")
for i in range(6):
    print(data["list"][i]["dt_txt"]+"：")
    print("温度:"+str(data["list"][i]["main"]["temp"])+"度")
    print("天气情况:"+data["list"][i]["weather"][0]["description"])
    print("最高温度:"+str(data["list"][i]["main"]["temp_max"])+"度")
    print("气压:"+str(data["list"][i]["main"]["pressure"])+"P")
    print("—————————————————————————————————————————————————————————")
future=input("是否查看未来4天的天气情况(是/否)：")
print("*********************************************************")
if future=='是':
    for i in range(32):
        print(data["list"][i+6]["dt_txt"]+"：")
        print("温度:"+str(data["list"][i+6]["main"]["temp"])+"度")
        print("天气情况:"+data["list"][i+6]["weather"][0]["description"])
        print("最高温度:"+str(data["list"][i+6]["main"]["temp_max"])+"度")
        print("气压:"+str(data["list"][i+6]["main"]["pressure"])+"P")
        print("—————————————————————————————————————————————————————————")
if future=='否':
    print("再见！欢迎再次使用天气查询系统")






















