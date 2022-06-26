from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Employee)
class EmployeeTranslation(TranslationOptions):
    fields = ('position', )


@register(NewTechno)
class NewTechnoTranslation(TranslationOptions):
    fields = ('project_title', 'text')

@register(Projects)
class ProjectsTranslation(TranslationOptions):
    fields = ('project_name',)

@register(Portfolio)
class PortfolioTranslation(TranslationOptions):
    fields = ('project_title', 'text')

@register(Partners)
class PartnersTranslation(TranslationOptions):
    fields = ('partner_description',)

@register(Media)
class MediaTranslation(TranslationOptions):
    fields = ('title',)

@register(PortFolioCompanies)
class PortFolioCompaniesTranslation(TranslationOptions):
    fields = ('project_title', 'text')

@register(InternationalCongresses)
class InternationalCongressesTranslation(TranslationOptions):
    fields = ('title', 'text')

@register(Quotes)
class QuotesTranslation(TranslationOptions):
    fields = ('quote',)

@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', )

@register(FullDescription)
class FullDescriptionTranslation(TranslationOptions):
    fields = ('text', )



