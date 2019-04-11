import re
from scrapy import Selector
import requests

url = 'http://www.mafengwo.cn/hotel/ajax.php?iMddId=10099&iAreaId=-1&iRegionId=-1&iPoiId=&position_name=&nLat=0&nLng=0&iDistance=10000&sCheckIn=2019-05-19&sCheckOut=2019-05-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&iPriceMin=&iPriceMax=&sTags=&sSortType=comment&sSortFlag=DESC&has_booking_rooms=0&has_faved=0&sKeyWord=&iPage=1&sAction=getPoiList5&_ts=1554907489439&_sn=f01809d556&_ts=1554907489440&_sn=fa07e689c1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
           'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
response = requests.get(url=url, headers=headers)
response.text.encode('gbk')
print(response.text)