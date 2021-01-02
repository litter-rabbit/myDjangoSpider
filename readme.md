  
创建新的app模块 
    python manage.py startapp newAppName
windows导出包列表 pip freeze > pipinstallmodel.txt
    安装包命令 pip install -r pipinstallmodel.txt
数据库<->模型
    python manage.py migrate # 建立数据库表（django有些自带的表需要创建）
    python manage.py inspectdb > spiderApp/models1.py # 数据库逆向到模型
创建后台admin账户
    python manage.py createsuperuser
    之后正常输入即可
密码忘记
    1.在程序的文件夹下，执行这样的命令，进行shell窗口：
        python manage.py shell
    2.对admin用户进行修改密码：
        from django.contrib.auth.models import User  
        user =User.objects.get(username='admin')  
        user.set_password('Spiderappstore1!')  
        user.save() 
ip代理有
    https://www.89ip.cn/ti.html #有接口, 直接复制即可
    https://www.7yip.cn/ # 建议使用https
    INSERT INTO .`proxy`(`ip`, `port`) VALUES ('27.220.163.35', '9000');
        