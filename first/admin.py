from django.contrib import admin
from .models import *


class DescEmployee(admin.TabularInline):
    model = EmDescription


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [DescEmployee, ]


class DescNews(admin.TabularInline):
    model = FullDescription


class NewsAdmin(admin.ModelAdmin):
    inlines = [DescNews, ]


admin.site.register(News, NewsAdmin)
admin.site.register(Projects)
admin.site.register(Media)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Portfolio)
admin.site.register(Partners)
admin.site.register(NewTechno)
admin.site.register(PortFolioCompanies)
admin.site.register(InternationalCongresses)

