import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjangoSpider.settings')                                                        ##
    import django  ##
    django.setup()
    browers=[
        {'user_agent':""},
        {'user_agent':""},
    ]
    from spiderApp.models import Brower
    def set_proxy(user_agent,useful='1'):
        if Brower.objects.filter(user_agent=user_agent):
            print("以有浏览器")
        else:
            Brower(user_agent=user_agent,info="",useful=useful).save()


    # for p in browers:
    #     set_proxy(p['user_agent'])
