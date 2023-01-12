from django.db import models

# Create your models here. 
# max_length is must for CharField
# title is in database(mysql)
# ('name') is in admin

class Book(models.Model):  
	title = models.CharField('name', max_length=50, default='')
	price = models.DecimalField('price', max_digits=7, decimal_places=2)
	is_active = models.BooleanField('is_active', default=True)

	class Meta:
		db_table = 'book'

	def __str__(self):
		return'%s_%s'%(self.title, self.price)
		#title_price


class Author(models.Model):
	name = models.CharField('name', max_length=11, default='')
	age = models.IntegerField('age', default=0)
	email = models.EmailField('email', default='')



# ORM  模型层流程 先创建app
# 创建数据库 create database name;
# drop database name;
# show database;  desc table名字
# select * from book\G;
# exit 退出
# 修改setting.py DATABASE

# 在models.py 创建class models
# class name(models.Model):  
# 	字段名 =  models.CharField(‘name’, …)
# 每次修改迁移同步: 模型修改到数据库
# 生成迁移文件python3 manage.py makemigrations
# 执行迁移脚本 python3 manage.py migrate 运行migration文件夹里的文件(先运行一遍init)

# 编辑类型=> 数据库类型
# booleanField() => tinyint(1) (0)
# CharField() => varchar , (max_length obligatoir)
# DataField(auto_now/auto_now_add/default 三选一) => date  
# DecimalField(max_digits, decimal_places ) => decimal(x, y) 
# EmailField() => varchar
# IntegerField() => int 
# ImageField() => varchar(100) 存储路径
# TestField() => longtest 文章 不定长数据
# 问题处理
# 直接添加 退出
# 混乱: 删除migration里面的文件000?_xxx.py(除了 _init_.py)
#         删除数据库 drop database myapp;

