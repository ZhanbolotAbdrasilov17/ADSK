from django.contrib import admin
from .models import *

# Register your models here.
class DescEmployee(admin.TabularInline):
    model = Emdescription

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [DescEmployee, ]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project)
admin.site.register(Portfolio)
admin.site.register(Partners)

class DescNews(admin.TabularInline):
    model = Fulldescription


class NewsAdmin(admin.ModelAdmin):
    inlines = [DescNews, ]

admin.site.register(News, NewsAdmin)
