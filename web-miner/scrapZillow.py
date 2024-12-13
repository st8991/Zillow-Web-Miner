# Created by Sam Tucker Dec 4 2024
import requests
import json
import time

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
cookie:zguid=24|%2462cced27-6773-4c4e-a810-c39b67176026; zjs_anonymous_id=%2262cced27-6773-4c4e-a810-c39b67176026%22; zjs_user_id=null; zg_anonymous_id=%221c5d4ef9-56f9-4315-b16d-3080e91e82e8%22; _ga=GA1.2.492688919.1731699743; _gid=GA1.2.771226549.1731699743; _pxvid=b790886d-a389-11ef-80b3-d5da4754fb53; _gcl_au=1.1.918855556.1731699744; _scid=jI5mT7toUMX6_WD4jeydfXaTIsr5_7Jp; _tt_enable_cookie=1; _ttp=0DyijE8GNxhuLauG7ZI3TBPt-LV.tt.1; _pin_unauth=dWlkPVpUVTJZakl6TWprdE16TXhNQzAwWldRekxUbGlOR0V0TURRMFpESmlPVGMwWWpnMQ; _ScCbts=%5B%5D; _fbp=fb.1.1731699745051.3607842672475906; _sctr=1%7C1731650400000; _lr_env_src_ats=false; zgsession=1|119857f3-121b-4603-9940-9b982f364100; pxcts=943191dc-a436-11ef-89b8-f887201bf4d0; JSESSIONID=46A3F615872E2D304280D2CEDF128404; _clck=1gasmhi%7C2%7Cfqx%7C0%7C1780; DoubleClickSession=true; _rdt_uuid=1731699744504.703a7f84-d91c-4418-b4f2-2fa16d2dabe0; _scid_r=lw5mT7toUMX6_WD4jeydfXaTIsr5_7JpSNSqvg; AWSALB=qViVFUISGaX90lUb8oTJ9agWIDrSAfuzRrsBtj9ddLdgye7p7ohqM3cgZ+zorQs3pc8oLwO3Gp1ZeqIFU5dIbBijUdrsExCDSOPQd2HGOJriPadu+kvVOr8O9Lvk; AWSALBCORS=qViVFUISGaX90lUb8oTJ9agWIDrSAfuzRrsBtj9ddLdgye7p7ohqM3cgZ+zorQs3pc8oLwO3Gp1ZeqIFU5dIbBijUdrsExCDSOPQd2HGOJriPadu+kvVOr8O9Lvk; _uetsid=bce61370a38911efb0df910bd0267c32; _uetvid=bce68ad0a38911efa9a2b91466140fb2; _px3=865f9f65a9a8e25947028c75ab862051b2402f74f4f12444f8369e4faa3dc3eb:dpwq189kffZQixKxu+euruuVTUtiLrksSpLqYf0Cle+lMBQV3Pj2ouExfE3MP5kM0E3n+2E04KYHzNidh5gyzQ==:1000:Sz7A2xCv7OlHSko9XvxensepQl+wJH8NHGSSLcS4aV++paFgjYJSkdrh3TpYcK7fS3Z70ISeOaxJOW3PRa3c6Yi+wTcbkkfB+TEJzVspJyzcKHGGCHGe5JMA/Y+fdh71S+dQZroG8WcUZ9eQ1ypUl3aTMO32qDaSpWie7Z7UOB1V+K8xtancovNNBXLMyL8gMtvVxx6r2dh68deMwJofNdJLdV4SuJk6J/bwYDGcacs=; __gads=ID=6d627bd7228082fb:T=1731699754:RT=1731778584:S=ALNI_MaQ2EY3nd9lOEGijbU1zZIJljm_XA; __gpi=UID=00000f95ed62ee6a:T=1731699754:RT=1731778584:S=ALNI_MYpViI0oM4WIR6cWPHmtwObt-1CwQ; __eoi=ID=f2e11574c21188bd:T=1731699754:RT=1731778584:S=AA-AfjYXyAPMi7DYE4f9zKKK44dR; search=6|1734370704109%7Crect%3D42.229786589144794%2C-86.92856675585938%2C41.43577538485671%2C-88.53531724414063%26rid%3D17426%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26showcase%3D0%26featuredMultiFamilyBuilding%3D0%26onlyRentalStudentHousingType%3D0%26onlyRentalIncomeRestrictedHousingType%3D0%26onlyRentalMilitaryHousingType%3D0%26onlyRentalDisabledHousingType%3D0%26onlyRentalSeniorHousingType%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0917426%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _clsk=trfl1j%7C1731778713874%7C9%7C0%7Cs.clarity.ms%2Fcollect
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