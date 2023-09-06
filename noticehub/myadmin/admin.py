from django.contrib import admin
from myadmin.models import Notice
from myadmin.models import Register

admin.site.site_header = 'Notice Hub Web App'
admin.site.index_title ='Master Admin Panel'


class NoticeAdmin(admin.ModelAdmin):
	list_display = ['id','subject','description','created_at','updated_at']

class RegisterAdmin(admin.ModelAdmin):
	list_display = ['id','name','email','contact','created_at']
	search_fields  =['name','email']

admin.site.register(Register,RegisterAdmin)
admin.site.register(Notice,NoticeAdmin)
