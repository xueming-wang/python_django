from django.shortcuts import render
from .models import Book

# Create your views here.
def all_book(request):
	all_book = Book.objects.all()
	return render(request, 'bookstore/all_book.html', all_book)
	



# a1 = Book.objects.all()
# for book in a1: 
# 	print(book.title)

#返回元组数据
# a2 = Book.objects.values_list('title', 'price')
# for book in a2:
# 	print(book[0]) # 所有的title

# a3 = Book.objects.order_by('-price') ->排序(降序)
# a3 = Book.objects.values('title').order_by('-price') ->排序(价格降序, 不显示价格)

# a4 = Book.objects.filter(price=20, title="xue") ->过滤(价格为20 and 名字为xue)
# a5 = Book.objects.get(price=20) ->过滤(价格为2) 但是只返回一个对象 -> try 保护

#非等值查询 双下滑线 __
# !!! a6 = Book.objects.filter(price__gt=20) ->过滤(价格大于20)
# !!! a7 = Book.objects.filter(price__gte=20) ->过滤(价格大于等于20)
# !!! a8 = Book.objects.filter(price__lt=20) ->过滤(价格小于20)
# !!! a9 = Book.objects.filter(price__lte=20) ->过滤(价格小于等于20)
# !!! a10 = Book.objects.filter(title__in=['xue', 'ming']) ->过滤(名字为xue or ming)
# !!! a11 = Book.objects.filter(price__range=[20, 30]) ->过滤(价格在20-30之间)
# a12 = Book.objects.filter(price__isnull=True) ->过滤(价格为空)
# a13 = Book.objects.filter(price__isnull=False) ->过滤(价格不为空)
# a14 = Book.objects.filter(id__exact=1) ->id为1
# a15 = Book.objects.filter(id__iexact=1) ->id为1(忽略大小写)
# !!!! a16 = Book.objects.filter(name__contains='x') ->name包含x
# a17 = Book.objects.filter(id__icontains=1) ->id包含1(忽略大小写)
# !!! a18 = Book.objects.filter(id__startswith=1) ->id以1开头
# a19 = Book.objects.filter(id__istartswith=1) ->id以1开头(忽略大小写)
# !!! a20 = Book.objects.filter(id__endswith=1) ->id以1结尾
# a21 = Book.objects.filter(id__iendswith=1) ->id以1结尾(忽略大小写)


# CRUD 增删改查
# -MyModel.objects.create(属性1=值1, …)
# 成功/失败抛出异常
# -obj = MyModel()
#   修改/添加: obj.属性=值
#    保存: obj.save()
# Django shell : python3 manage.py shell —>
# 	 from bookstore.models import Book
# 	 运行MyModel.objects.create(属性1=值1, …)
# 	  exit()

