from django.contrib import admin
from .models import *


class DescEmployee(admin.TabularInline):
    model = EmDescription


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [DescEmployee, ]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Portfolio)
admin.site.register(Partners)
admin.site.register(NewTechno)


class DescNews(admin.TabularInline):
    model = FullDescription


class NewsAdmin(admin.ModelAdmin):
    inlines = [DescNews, ]


admin.site.register(News, NewsAdmin)
admin.site.register(Projects)
