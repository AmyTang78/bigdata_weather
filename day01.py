# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:58:19 2018

@author: lenovo
"""

import urllib.request as r
import json
 #全球天气app
print("欢迎使用全球天气app")   
city=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'   
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
data=json.loads(info)
print("温度:"+str(data["main"]["temp"])+"度")
print("天气情况:"+data["weather"][0]["description"])
print("最高温度:"+str(data["main"]["temp_max"])+"度")
print("气压:"+str(data["main"]["pressure"]))
