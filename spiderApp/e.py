import json

import redis
from redis import StrictRedis

from spiderApp.Redis_ import Set_Request_Url
from spiderApp.models import Appdata

pool = redis.ConnectionPool(host='10.13.88.111',port = 6379, db =1)
def Set_Request_Url(dict_data):
    conn = StrictRedis(connection_pool=pool)
    is_have=Search_url(dict_data["appId"])
    if not is_have:
        conn.rpush("infos", str(dict_data))
    else:
        print(dict_data)
    return True
def Search_url(ID):
    results=[]
    num=10000
    conn = StrictRedis(connection_pool=pool)
    urlst = conn.lrange("infos", 0, num)
    all=conn.llen('infos')
    for url in urlst:
        data=eval(str(url.decode('utf-8')))
        if str(data['appId']) == str(ID):
            results.append(data['appId'])
    if len(results)==1:
        return True
    else:
        num+=10000
        if all<num:
            return False
        else:
             return  Search_url(ID)
    return False

collection = Appdata._get_collection()
def get_all():
    lists=[]
    collection = Appdata._get_collection()
    count = collection.find({}).skip(1)
    for i in count:
        lists.append(i)
    return lists
def ui(i):
    info = {'appId': i['_id'], 'appName':i['app_name']}
    Set_Request_Url(info)
from multiprocessing import Pool
if __name__=="__main__":
    pool=Pool(8)
    lists=get_all()
    print(type(lists))
    pool.map(ui,lists)