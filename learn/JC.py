views.py
处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。

urls.py
网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数

models.py
与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用

forms.py
表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作，当然你也可以不使用

templates 文件夹
views.py 中的函数渲染templates中的Html模板，得到动态内容的网页，当然可以用缓存来提高速度

admin.py
后台，可以用很少量的代码就拥有一个强大的后


# 新建一个django project
django-admin.py startproject project-name

#新建 app
python manage.py startapp app-name or django-admin.py startappp app-name

#同步数据库
python manage.py syncdb
#Django 1.7.1及以上的需以下命令
python manage.py makemigrations
python mamnage.py migrate

#使用开发服务器
python manage.py runserver
# 当提示端口被占用的时候，可以用其它端口：
python manage.py runserver 8001
python manage.py runserver 9999
（当然也可以kill掉占用端口的进程）

# 监听所有可用 ip （电脑可能有一个或多个内网ip，一个或多个外网ip，即有多个ip地址）
python manage.py runserver 0.0.0.0:8000
# 如果是外网或者局域网电脑上可以用其它电脑查看开发服务器
# 访问对应的 ip加端口，比如 http://172.16.20.2:8000

#清空数据库
python manage.py flush

#创建超级管理员
python manage.py createsuperuser

# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填

# 修改 用户密码可以用：
python manage.py changepassword username

#导出数据 导入数据
pyton manage.py dumpdate appname > appname.json
pytohn mamage.py loaddata appname .jsom

#Django 项目环境
python manage .py shell

#数据库命令行
python manag.py dbshell







