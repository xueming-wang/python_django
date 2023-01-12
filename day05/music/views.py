from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_view(request):
	return render(request, 'music/index.html')



# app 分布式路由
# —creer nouveau app dans le fichier

# 创建python3 manage.py startapp newapp  

# 配置
# INSTALLED_APPS= [
# 	‘newapp’
# ]

# 主路由urls.py 
# path('music/', include('music.urls'))

# 在newapp 里creer urls.py in app
# from django.urls import path
# from . import views
# urlpatterns = [
#     #http://127.0.0.1:8000/music/index
#     path('index', views.index_view),
# ]

# 在 newapp里面创建 templates 文件夹里在创建一个appname 的文件夹里面写html 文件防止和外层template重名