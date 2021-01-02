from spiderApp.Redis_ import Set_Request_Url
import os
import random

if __name__ == '__main__':

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjangoSpider.settings')                                                        ##
    import django  ##
    django.setup()
    from spiderApp.models import Appdata, Comment
    #查看全部
    print("APP",len(Appdata.objects.all()))#120017
    print("Comment",len(Comment.objects.all()))#3590
    # 导出

    # def mysql_get_data():
    #     # lists=[]
    #     import pymysql
    #     conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db="spiderappstore", charset="utf8")  # 链接
    #     cur = conn.cursor()
    #     sql='select * from comment'
    #     cur.execute(sql)
    #     num=0
    #     for i in cur.fetchall():
    #         num+=1
    #         if Comment.objects.filter(comment_id=i[0]):
    #             continue
    #         else:
    #             print(i,num)
    #             Comment(comment_id=i[0],
    #                     app_store=i[1],
    #                     comment_info=i[2],
    #                     stars=i[3],
    #                     app_id=i[4],
    #                     ).save()
    #         # lists.append(data)
    #     # return lists
    # mysql_get_data()
