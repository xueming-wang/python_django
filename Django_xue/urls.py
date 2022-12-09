"""Django_xue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path #
from . import views

urlpatterns = [
    #path(route, views, name=None)
    path('admin/', admin.site.urls),

    path('', views.index_view),
    path('page/1', views.page1),

    #converter 1-100 PAGE
    # path('page/<int:page>', views.pageXXX)
    path('page/<int:pg>', views.page_view),
    ### <str:username>     
    ### <int:page>
  
    #正则表达式匹配
    #re_path(reg, view, name=  )  reg is string
    #/20/mul/40  只允许有1-两位数
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),

    #/int/add/int  
    path('<int:n>/<str:op>/<int:m>', views.cal_view),

]
