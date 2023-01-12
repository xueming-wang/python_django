from django.contrib import admin
from .models import *


# python3 manger.py createsuperuser
# http://localhost:8000/admin
# admin 显示'%s_%s'%(self.title, self.price)
#管理自己定义的class  modelo
# -- from .models import Book
# -- class XXXmangager(admin.ModelAdmin)
# admin.site.register(Mymodele, XXXmangager)

 
# gestion , register de modèles
class BookMangager(admin.ModelAdmin):
	#show list in admin
	list_display = ['id', 'title', 'price']
	# 默认在id上 links 可链接到修改页面 
	list_display_links = ['title']
	# 过滤器filtre show by 'price'
	list_filter = ['price']
	# 搜索框 search by 'title'[模糊查询]
	search_fields = ['title']
	# 在列表可编辑的字段, 不能和links同时使用
	list_editable = ['price']

# admin 添加自己的model
admin.site.register(Book, BookMangager)

