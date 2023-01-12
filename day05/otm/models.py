from django.db import models

# Create your models here.

# 一对多
# otm_pub 
class Pub(models.Model):
	name = models.CharField('pubname', max_length=50)

# otm_book  
class Book(models.Model):
	title = models.CharField('bookname', max_length=11)
	pub = models.ForeignKey(Pub, on_delete=models.CASCADE)

# 创建数据
# from .models import *
pub1 = Pub.objects.create(name='pub1')
b1 = Book.objects.create(title='book1', pub=pub1)
Book.objects.create(title='book2', pub_id=1)


# 查询数据
# b1 = Book.objects.get(id='1')
# print(b1.pub.name) # pub1的name
# # 反向查询 -> 带有外键的所有的书
# books = pub1.book_set.all() #book_set 为外键的值
# book2 = Book.objects.filter(pub=pub1) #filter 过滤
# for book in books:
# 		print(book2.title)
# in shell:  b1.pub.name # 'pub1'