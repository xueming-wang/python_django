from django.db import models

# Create your models here.
# 关系映射 : 一对一, 一对多, 多对多
# on_delete ->级联删除
# on_delete=models.CASCADE  ->级联删除(全删)
# on_delete=models.PROTECT  ->保护(不删, 报错)
# on_delete=models.SET_NULL  ->设置为null ()

# 一对一 creer model 
class Author(models.Model):
	#wife 发向属性
	name = models.CharField('name', max_length=11)

# wify model => in database author_id | int 
class Wife(models.Model):
	name = models.CharField('name', max_length=11)
	author = models.OneToOneField(Author, on_delete=models.CASCADE)

#创建数据
# a = Author(name='alex')
# w = Wife.objects.create(name='xue', author=a) #关联object
# w = Wife.objects.create(name='xue', author_id=1)#关联id

# 查询search data
# wife = Wife.objects.get(name='ming')
# print(wife.author.name)  # author 的name
# 反向查询
# a.wife.name (外键的值)


# 一对多


# 多对多
