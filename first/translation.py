from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Sotrudniki)
class SotrudnikiTranslation(TranslationOptions):
    fields = ('position', )


@register(NovyeTehnologii)
class NovyeTehnologiiTranslation(TranslationOptions):
    fields = ('project_title', 'text')

@register(Proekty)
class ProektyTranslation(TranslationOptions):
    fields = ('project_name',)

@register(Portfolio)
class PortfolioTranslation(TranslationOptions):
    fields = ('project_title', 'text')

@register(Partners)
class PartnersTranslation(TranslationOptions):
    fields = ('partner_description',)

@register(Smi)
class SmiTranslation(TranslationOptions):
    fields = ('title',)

@register(PortFolioCompanies)
class PortFolioCompaniesTranslation(TranslationOptions):
    fields = ('project_title', 'text')

@register(MezhdunarodnyeKon)
class MezhdunarodnyeKonTranslation(TranslationOptions):
    fields = ('title', 'text')

@register(Tchitaty)
class TchitatyTranslation(TranslationOptions):
    fields = ('quote',)

@register(Novosti)
class NovostiTranslation(TranslationOptions):
    fields = ('title', )

@register(FullDescription)
class FullDescriptionTranslation(TranslationOptions):
    fields = ('text', )


@register(TchitatyMenedzherov)
class TchitatyMenedzherovTranslation(TranslationOptions):
    fields = ('job_title', 'text', )

@register(VideoContent)
class VideoContentTranslation(TranslationOptions):
    fields = ('text', )


