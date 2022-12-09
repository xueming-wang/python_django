from django.http import HttpResponse


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
    