from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


@admin.register(Employee)
class EmployeeAdmin(TranslationAdmin):
    pass


@admin.register(NewTechno)
class NewTechnoAdmin(TranslationAdmin):
    pass

@admin.register(Projects)
class ProjectsAdmin(TranslationAdmin):
    pass

@admin.register(Quotes)
class QuotesAdmin(TranslationAdmin):
    pass


@admin.register(ManagersQuotes)
class ManagersQuotesAdmin(TranslationAdmin):
    pass


@admin.register(InternationalCongresses)
class InternationalCongressesAdmin(TranslationAdmin):
    pass

@admin.register(PortFolioCompanies)
class PortFolioCompaniesAdmin(TranslationAdmin):
    pass

@admin.register(Partners)
class PartnersAdmin(TranslationAdmin):
    pass

@admin.register(Portfolio)
class PortfolioAdmin(TranslationAdmin):
    pass

@admin.register(Smi)
class SmiAdmin(TranslationAdmin):
    pass

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    pass

@admin.register(FullDescription)
class FullDescriptionAdmin(TranslationAdmin):
    pass

@admin.register(VideoContent)
class VideoContentAdmin(TranslationAdmin):
    pass

class DescEmployee(admin.TabularInline):
    model = EmDescription


# class EmployeeAdmin(admin.ModelAdmin):
#     inlines = [DescEmployee, ]


class DescNews(admin.TabularInline):
    model = FullDescription


class NewsAdmin(admin.ModelAdmin):
    inlines = [DescNews, ]


admin.site.register(NewsPictures)
admin.site.register(RezultatyOblastey)

