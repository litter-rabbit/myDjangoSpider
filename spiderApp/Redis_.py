import json
import time

import redis
from redis import StrictRedis

pool = redis.ConnectionPool(host='10.13.88.111',port = 6379, db =0)
def Set_Request_Url(dict_data):
    conn = StrictRedis(connection_pool=pool)
    conn.rpush("RequestList", str(dict_data))
    return True


def Search_Request_Url(sort,app_store,request_type):
    results=[]
    conn = StrictRedis(connection_pool=pool)
    lists=conn.lrange("RequestList",0,-1)
    #print(lists)
    for url in lists:
        data = eval(str(url.decode('utf-8')))
        if str(data['sort'])==str(sort) and data['app_store']==app_store and data['request_type']==request_type:
            results.append(data['url'])
    return results



def Search_url(urls,num):
    results=[]
    conn = StrictRedis(connection_pool=pool)
    urlst = conn.lrange("RequestList", 0, num)
    all=conn.llen('RequestList')
    for url in urlst:
        data=eval(str(url.decode('utf-8')))
        if str(data['url']) == str(urls):
            results.append(data['url'])
    if len(results)==1:
        return results
    else:
        num+=10000
        if all<num:
            return []
        else:
             return  Search_url(urls,num)
