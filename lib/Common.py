import json
from urllib.request import urlopen
from urllib import request

def getBitCoin():
    print('[INFO]:Start to get infos from API ')
    ipAddress ="https://www.bitstamp.net/api/ticker/"
    response = urlopen(ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    lastprice=responseJson.get("last")+ '$'
    print('[INFO]: Data send function successfully...')
    return responseJson

def get_stock_data(id,scale,data_len):
    symsol = '股票代码'
    scale = scale
    data_len = data_len
    url = 'http://quotes.sina.cn/cn/api/json_v2.php/CN_MarketDataService.getKLineData?symbol={0}&scale={1}&datalen={2}'.format(id, scale, data_len)
    req = request.Request(url)
    rsp = request.urlopen(req)
    res = rsp.read()
    res_json = json.loads(res)
    bar_list = []
    res_json.reverse()
    print(res_json)
    return res_json