# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:40:37 2018

@author: th
"""
#全球天气查询系统
#导入包
import urllib.request as r
import json
from xpinyin import Pinyin
city=input("欢迎使用天气查询系统，请输入城市：")
#将中文转换为拼音
pin = Pinyin()
city_1 = pin.get_pinyin(city,"")
#获取天气
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
#联网
info=r.urlopen(url.format(city_1)).read().decode('utf-8','ignore')
#字符串转字典
data=json.loads(info)
print("今日天气情况如下：")
#for循环输出天气情况
for i in range(len(data['list'])-32):
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
        print(data["list"][i+len(data['list'])-32]["dt_txt"]+"：")
        print("温度:"+str(data["list"][i+len(data['list'])-32]["main"]["temp"])+"度")
        print("天气情况:"+data["list"][i+len(data['list'])-32]["weather"][0]["description"])
        print("最高温度:"+str(data["list"][i+len(data['list'])-32]["main"]["temp_max"])+"度")
        print("气压:"+str(data["list"][i+len(data['list'])-32]["main"]["pressure"])+"P")
        print("—————————————————————————————————————————————————————————")
if future=='否':
    print("再见！欢迎再次使用天气查询系统")
input("输入任意代码退出......")
























