import requests

def GetGeoLocation(address="武汉大学", out_type="json"):
    url=F'http://api.map.baidu.com/geocoder?address={address}&zoom=9&output={out_type}&src=webapp.baidu.openAPIdemo'
    r=requests.get(url).json()
    return r["result"]["location"]["lng"], r["result"]["location"]["lat"] 

def GetMapUrl(address="武汉大学"):
    title = "我的位置"
    lng, lat = GetGeoLocation(address, out_type="json")
    url = F"http://api.map.baidu.com/marker?location={lng},{lat}&title={title}&content={address}&output=html&src=webapp.baidu.openAPIdemo   "
    # print(url)
    return url