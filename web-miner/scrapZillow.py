# Created by Sam Tucker Dec 4 2024
import requests
import json
import time
import os

def convert_headers(raw_header):
    header = dict()
    for line in raw_header.split("\n"):
        if ":" in line:
            a, b = line.split(":", 1)
            header[a.strip()] = b.strip()
    return header

url = 'https://www.zillow.com/async-create-search-page-state'
rawHeader = '''accept:*/*
accept-encoding:gzip, deflate, br, zstd
accept-language:en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
content-length:450
content-type:application/json
origin:https://www.zillow.com
priority:u=1, i
referer:https://www.zillow.com/chicago-il/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-88.53531724414063%2C%22east%22%3A-86.92856675585938%2C%22south%22%3A41.43577538485671%2C%22north%22%3A42.229786589144794%7D%2C%22usersSearchTerm%22%3A%22Chicago%2C%20IL%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A17426%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D
sec-ch-ua:"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"
sec-ch-ua-mobile:?0
sec-ch-ua-platform:"Windows"
sec-fetch-dest:empty
sec-fetch-mode:cors
sec-fetch-site:same-origin
user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'''
header = convert_headers(rawHeader)
# Zillow's bot protection needs a browser cookie: copy it from your browser's dev tools
header['cookie'] = os.environ['ZILLOW_COOKIE']

pageNum=1 
nextPage=True
#Manhattan, New York, NY
while nextPage:
    file=open('mtnZillowSearch'+str(pageNum)+'.json','w')
    dataMTN = '''{"searchQueryState":{"pagination":{"currentPage":'''+str(pageNum)+'''},"isMapVisible":true,"mapBounds":{"west":-74.22223833251951,"east":-73.73540666748045,"south":40.601680182175244,"north":40.95939719577998},"mapZoom":11,"regionSelection":[{"regionId":12530,"regionType":17}],"filterState":{"sortSelection":{"value":"days"},"isMultiFamily":{"value":false},"isLotLand":{"value":false},"isManufactured":{"value":false}},"isListVisible":true},"wants":{"cat1":["listResults","mapResults"],"cat2":["total"]},"requestId":4,"isDebugRequest":false}'''
    r = requests.put(url, data=dataMTN, headers=header)
    print('Manhattan',pageNum,'---',r.status_code)
    file.write(r.content.decode()+'\n')
    nextPage=json.loads(r.text).get('cat1').get('searchList').get('pagination').get('nextUrl')
    pageNum+=1
    file.close()
    time.sleep(1)
#Brooklyn, New York, NY
pageNum=1 
nextPage=True
while nextPage:
    file=open('bkZillowSearch'+str(pageNum)+'.json','w')
    dataBK='''{"searchQueryState":{"pagination":{"currentPage":'''+str(pageNum)+'''},"isMapVisible":true,"mapBounds":{"west":-74.05942291625975,"east":-73.81600708374022,"south":40.56538304677886,"north":40.74457975576221},"mapZoom":12,"regionSelection":[{"regionId":37607}],"filterState":{"sortSelection":{"value":"days"},"isMultiFamily":{"value":false},"isLotLand":{"value":false},"isManufactured":{"value":false}},"isListVisible":true},"wants":{"cat1":["listResults","mapResults"],"cat2":["total"]},"requestId":5,"isDebugRequest":false}    r = requests.put(url, data=dataMTN, headers=header)'''
    r = requests.put(url, data=dataBK, headers=header)
    print('Brooklyn',pageNum,'---',r.status_code)
    file.write(r.content.decode()+'\n')
    nextPage=json.loads(r.text).get('cat1').get('searchList').get('pagination').get('nextUrl')
    pageNum+=1
    file.close()
    time.sleep(1)
#Queens, New York, NY
pageNum=1 
nextPage=True
while nextPage:
    file=open('qnZillowSearch'+str(pageNum)+'.json','w')
    dataQN = '''{"searchQueryState":{"isMapVisible":true,"mapBounds":{"north":40.850253934774095,"south":40.49194820605614,"east":-73.58803616748048,"west":-74.07486783251954},"mapZoom":11,"filterState":{"sortSelection":{"value":"days"},"isMultiFamily":{"value":false},"isLotLand":{"value":false},"isManufactured":{"value":false}},"isListVisible":true,"regionSelection":[{"regionId":270915,"regionType":17}],"pagination":{"currentPage":'''+str(pageNum)+'''}},"wants":{"cat1":["listResults","mapResults"],"cat2":["total"]},"requestId":16,"isDebugRequest":false}'''
    r = requests.put(url, data=dataQN, headers=header)
    print('Queens',pageNum,'---',r.status_code)
    file.write(r.content.decode()+'\n')
    nextPage=json.loads(r.text).get('cat1').get('searchList').get('pagination').get('nextUrl')
    pageNum+=1
    file.close()
    time.sleep(1)
#Staten Island, New York, NY
pageNum=1 
nextPage=True
while nextPage:
    file=open('siZillowSearch'+str(pageNum)+'.json','w')
    dataSI = '''{"searchQueryState":{"isMapVisible":true,"mapBounds":{"north":40.66206832403046,"south":40.48264988899286,"east":-74.03223908374022,"west":-74.27565491625975},"mapZoom":12,"filterState":{"sortSelection":{"value":"days"}},"isListVisible":true,"category":"cat1","regionSelection":[{"regionId":27252,"regionType":17}],"pagination":{"currentPage":'''+str(pageNum)+'''}},"wants":{"cat1":["listResults","mapResults"],"cat2":["total"]},"requestId":29,"isDebugRequest":false}'''
    r = requests.put(url, data=dataSI, headers=header)
    print('Staten Island',pageNum,'---',r.status_code)
    file.write(r.content.decode()+'\n')
    nextPage=json.loads(r.text).get('cat1').get('searchList').get('pagination').get('nextUrl')
    pageNum+=1
    file.close()
    time.sleep(1)
#The Bronx, New York, NY
pageNum=1 
nextPage=True
while nextPage:
    file=open('brxZillowSearch'+str(pageNum)+'.json','w')
    dataBRX = '''{"searchQueryState":{"isMapVisible":true,"mapBounds":{"north":40.93963065878772,"south":40.76095957650412,"east":-73.72773358374022,"west":-73.97114941625975},"mapZoom":12,"filterState":{"sortSelection":{"value":"days"}},"isListVisible":true,"category":"cat1","regionSelection":[{"regionId":17182,"regionType":17}],"pagination":{"currentPage":'''+str(pageNum)+'''}},"wants":{"cat1":["listResults","mapResults"],"cat2":["total"]},"requestId":33,"isDebugRequest":false}'''
    r = requests.put(url, data=dataBRX, headers=header)
    print('The Bronx',pageNum,'---',r.status_code)
    file.write(r.content.decode()+'\n')
    nextPage=json.loads(r.text).get('cat1').get('searchList').get('pagination').get('nextUrl')
    pageNum+=1
    file.close()
    time.sleep(1)