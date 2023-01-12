from django.db import models

# Create your models here
# 多对多
# 数据库
#  mtm_author                 
#  mtm_book                   
#  mtm_book_authors  
class Author(models.Model):
	name = models.CharField('name', max_length=11)

class Book(models.Model):
	title = models.CharField('bookname', max_length=11)
	authors = models.ManyToManyField(Author)

# 第三方tables
# ----------+------+------+-----+---------+----------------+
# | id        | int  | NO   | PRI | NULL    | auto_increment |
# | book_id   | int  | NO   | MUL | NULL    |                |
# | author_id |

# 创建数据 :方案一
# 创建autor 再关联book
	# author1 = Author.objects.create(name='alex')
	# author2 = Author.objects.create(name='egon')
# 在绑定:两个author同时写了一本呢书 
	# book = author1.book_set.create(title='book1')
	# author2.book_set.add(book)

# 创建数据 :方案二
# 创建book 再关联author
	# book = Book.objects.create(title='book1')
	# author1 = book.objects.create(name='alex')
	# book.authors.add(author1)

# 查询数据
# book.authors.all() #获取book对应的所有author信息
# book.authors.filter(age__gt=18) #获取book对应的所有author信息, 并且age>18
# 反向
# 通过auther 查询书 -> book_set
# author.book_set.all() #获取author对应的所有book信息
# author.book_set.filter(price__gt=100) #获取author对应的所有book信息, 并且price>100