from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render #模板层


# view 是视图函数
# request 是请求对象
# HttpResponse 是响应对象
# 接收请求, 获取数据, 返回响应 , 丢给模板层


POST_FROM = '''
<form action="/test_get_post" method="post">
    username: <input type="text" name="username">
    <input type="submit" value="提交">
</form>
'''


# 视图函数
def index_view(request): 
    html = '<h1>PAGE SHOUYE</h1>'
    return HttpResponse(html)

def page1(request): 
    html = '<h1>page 1</h1>'
    return HttpResponse(html)

def page_view(request, pg): 
    html = 'this is %s page!' %(pg)
    return HttpResponse(html)

def cal_view(request, n, op, m):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('Your op is wrong')
    
    result = 0
    if op == 'add':
        result = n + m
    elif op == 'sub':
        result = n - m
    elif op == 'mul':
        result = n * m
    return HttpResponse('le resultat is %s'%(result))


def cal2_view(request, x, op, y):
    html = 'x:%s op:%s y:%s'%(x, op, y)
    return HttpResponse(html)


# def test_request(request):
#    print('method is: ', request.method) #GET
#    print('request.GET is :', request.GET) #<QueryDict: {}>
#    print('path_info is: ', request.get_full_path) # /test_request?i=1&j=2
#    

#  response 重定向
#   return HttpResponseRedirect('/page/1')


def test_get_post(request):
    if request.method == 'GET':
        # print(request.GET['a'])  # 1 
        # print(request.GET.get('b', 'no b')) # 不确定有没有b用get()
        # print(request.GET.getlist('c')) # 多个c的值, <QueryDict: {'c' :['1','2','3']}>
        return HttpResponse(POST_FROM) #返回表单

    elif request.method == 'POST': #提交表单
        # print(request.POST['a'])
        # print(request.POST.get('a', 'no b'))
        # print(request.POST.getlist(''))
        #提交表单
        print ('username is: ', request.POST['username']) 
        return HttpResponse('post ok')
    else:
        return HttpResponse('ok')


#test html 方案二
def test_html(request):
    #数据从数据库拿出来
    dic = {'name':'zhangsan', 'age':18}
   
    return render(request, 'test_html.html', dic)
    #第三个参数是字典, 传递给模板的数据


def test_html_param(request):

    dic = {}  #一个字典
    dic['int'] = 88
    dic['str'] = 'hello'
    dic['lst'] = ['a', 'b', 'c']
    dic['dict'] = {'a': 1, 'b': 2, 'c': 3}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()

    return render(request, 'test_html_param.html', dic)

def say_hi():
    return 'hahaha'

class Dog(object):
    def say(self):
        return 'wangwangwang'

def test_if_for(request):
    dic = {}
    dic['x'] = 10

    dic['lst'] = ['a', 'b', 'c']
    
    return render(request, 'test_if_for.html', dic)



def test_mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')

    elif request.method == 'POST':
        #获取网页数据
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']

        result = 0
        if op == 'add':
            result = int(x) + int(y)
        elif op == 'sub':
            result = int(x) - int(y)
        elif op == 'mul':
            result = int(x) * int(y)
        elif op == 'div':
            result = int(x) / int(y)
        else:
            result = 'op is wrong'

        #local() 函数会以字典类型全部局部变量
        return render(request, 'mycal.html', locals())

