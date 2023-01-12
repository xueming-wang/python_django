from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Book
from django.db.models import F, Q

# Create your views here.
def all_book(request):
	# all_book = Book.objects.all()
	# is_active is 有效数据
	all_book = Book.objects.filter(is_active=True)
	return render(request, 'bookstore/all_book.html', locals())
	

def update_book(request, book_id):
	# bookstore/update_book/1
	try:
		book = Book.objects.get(id=book_id, is_active= True)
	except Exception as e:
		print(e)
		return HttpResponse('book is not exist')
	if request.method == 'GET':
		return render(request, 'bookstore/update_book.html', locals())
	elif request.method == 'POST': 
		price = request.POST.get('price')
		book.price = price
		book.save()
		return HttpResponseRedirect('/bookstore/all_book')
		


#url /delete?book_id=xx
def delete_book(request):
	#获取要删除的book_id
	book_id = request.GET.get('book_id')
	if not book_id:
		return HttpResponse('book_id is not exist')
	try :
		book = Book.objects.get(id=book_id, is_active=True)
	except Exception as e:
		print(e)
		return HttpResponse('book is not exist')
	#伪删除就是更新
	book.is_active = False
	book.save()
	return HttpResponseRedirect('/bookstore/all_book')


#所以的书价格涨10/点赞+1
def add_like(request, id):
	id.like = F('like') + 1 #解决并发 不获取进行操作
	#update book set like = like + 1 where id = id
	id.save()

# F : 如果自身有两个数值 比较 -正常都取出来 两者进行比较
# def compare_prix(request):
# 	books = Book.objects.filter(maket_price__gt=F('price'))
# 	#select * from book where maket_price > price
# 	print(books)

# Q : 用于复杂的查询 |, &, ~
# 找出价格低于20 或者 名字中包含xue的书
# Book.objects.filter(Q(price__lt=20) | Q(title__contains='xue'))
#  &~ 与非 前面成立 且 后面不成立


#聚合查询:统计平均 总数...
# 整表聚合:  例如 select count(*) (as nn) from book;
# from django.db.models import Avg(平均), Max, Min, Sum(和), Count
# Book.objects.aggregate(result = Avg('price')) # price的平均值
# Book.objects.aggregate(result=Count('id')) # id的总数
# return dic { "result" : 值}

# 分组聚合 result 是有price的值
# 第一步分组 result = MyModel.objects.values('price')
# 显示所有的price [{'price': Decimal('3.00')}, {'price': Decimal('3.33')},...]

# 第二步聚合: mycount 是 有多少个id的price是一个值
# result.annotate(my_count = Count('id')) 
# <QuerySet [{'price': Decimal('3.00'), 'mycount': 3}, {'price': Decimal('3.33'), 'mycount': 1}, 

# 选择 > 1 的数据
# result.annotate(my_count = Count('id')).filter(my_cout__gt=1)



# 查询	
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

#修改更新
# b1 = MyModel.objects.get(id=1)
# b1.属性 = 值
# b1.save()
#批量修改
# MyModel.objects.filter(id=3).update(属性=值)
# MyModel.objects.all().update(属性=值)

#删除单一
# try :
#   c1 = MyModel.objects.get(id=1)
#   c1.delete()
# except:
# 	print("error")

# 批量删除


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

#查询
# -MyModel.objects.get(属性=值)


