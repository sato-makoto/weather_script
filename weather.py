 #!/usr/bin/env python3
import json

jdata = open('weather.json', 'r')
old_jdata = open('weather.json.old', 'r')
load_jdata = json.load(jdata)
load_old_jdata = json.load(old_jdata)

# print(json.dumps(load_jdata[0]['timeSeries'][0]['areas'][0]['weathers'], ensure_ascii=False))
today_weather = load_jdata[0]['timeSeries'][0]['areas'][0]['weathers'][0]
today_wind = load_jdata[0]['timeSeries'][0]['areas'][0]['winds'][0]
print("今日の天気は", today_weather)
print("今日の風", today_wind)
today_temp_low = load_old_jdata[0]['timeSeries'][2]['areas'][0]['temps'][0]
today_temp_high = load_jdata[0]['timeSeries'][2]['areas'][0]['temps'][1]
print("今朝の最低気温は", today_temp_low ," ℃,", "日中の最高気温は", today_temp_high, "℃")

print("")
# print(json.dumps(today_weather, ensure_ascii=False)[1:-1:])
rain_today = load_jdata[0]['timeSeries'][1]['areas'][0]['pops'][0:3]
print("雨の降る確率:  6時-12時は", rain_today[0], "%です")
print("雨の降る確率: 12時-18時は", rain_today[1], "%です")
print("雨の降る確率: 18時-24時は", rain_today[2], "%です")

