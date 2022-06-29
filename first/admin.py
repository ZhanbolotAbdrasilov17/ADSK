from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


@admin.register(Sotrudniki)
class SotrudnikiAdmin(TranslationAdmin):
    pass


@admin.register(NovyeTehnologii)
class NovyeTehnologiiAdmin(TranslationAdmin):
    pass

@admin.register(Proekty)
class ProektyAdmin(TranslationAdmin):
    pass

@admin.register(Tchitaty)
class TchitatyAdmin(TranslationAdmin):
    pass


@admin.register(TchitatyMenedzherov)
class TchitatyMenedzherovAdmin(TranslationAdmin):
    pass


@admin.register(MezhdunarodnyeKon)
class MezhdunarodnyeKonAdmin(TranslationAdmin):
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

@admin.register(Novosti)
class NovostiAdmin(TranslationAdmin):
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


admin.site.register(KartinkiNovostey)
admin.site.register(RezultatyOblastey)

