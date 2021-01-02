import os

from config.mysql_get_data import mysql_get_data

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjangoSpider.settings')                                                        ##
    import django  ##
    django.setup()
    proxys=[
        {'ip':"",'port':''},
        {'ip':"",'port':''},
    ]
    from spiderApp.models import Proxy
    def set_proxy(ip,port,http_type='http',useful='1'):
        if Proxy.objects.filter(ip=ip,port=port):
            print("以有代理")
        else:
            Proxy(ip=ip,port=port,useful=useful,http_type=http_type).save()



    # for p in proxys:
    #     set_proxy(p['ip'],p['port'])
