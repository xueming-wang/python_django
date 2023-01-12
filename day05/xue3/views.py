from django.shortcuts import render
from django.http import HttpResponse

def test_static(request):
	return render(request, 'test_static.html')



# 设置cookies :no secu
# ->服务器验证用户密码setcookie -> 给客户端并保存到客户端
# Cookis ->sauvgarder client -> CHROME = application->storage-> ‘Cookies’
# key = value(ASCII) 
# 有生命周期
# porter le cookies chaque fois envoyer a server 

def set_cookies(request):
	res = HttpResponse('设置cookies')
	res.set_cookie('name','xue3', 500)
	return res 
#reseau: Set-Cookie 存储
	
#修改cookies 过期时间两小时
# res =  HttpResponse('修改')
# res.set_cookie('新名字','名', 3600)
# return res

# 获取cookies ->如果没有返回默认值没有
def get_cookie(request):
	value = request.COOKIES.get('name', '没有')
	return HttpResponse(value)  #xue3

# delete cookies
# HttpResponse.delete_cookie(key)


# session->服务器保存每个用户信息->给客户端一个凭证(sessionid) ->客户端保存sessionid
# ->sessionid放进cookies->每次请求都会带上sessionid

# 设置session -> secu
# settings.py 配置 INSTALLED_APPS = ['django.contrib.sessions']
# settings.py 配置 MIDDLEWARE = ['django.contrib.sessions.middleware.SessionMiddleware']
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 7
# close web , session 失效
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# session is dic 
def set_session(request):
	request.session['name'] = 'ming'
	return HttpResponse('设置session')

def get_session(reqyest):
	value = reqyest.session.get('name', '没有')
	return HttpResponse(value)

# 保存
# request.session['key'] = value
# 获取
# request.session.get('key', '默认值')
# 删除
# del request.session['key']


# 定期删除SESSION:过期
# python3 manage.py clearsessions






 
