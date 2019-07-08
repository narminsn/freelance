from django.contrib import admin
from .models import MenuModel, HeaderModel, ContactModel, Contact_sessionModel, About_session, PortfolioModel, PortfolioItem, CopyrightModel, FooterModel, FooterIcon
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display=("title", "id")



admin.site.register(MenuModel, MenuAdmin)
admin.site.register(HeaderModel)
admin.site.register(ContactModel)
admin.site.register(Contact_sessionModel)
admin.site.register(About_session)
admin.site.register(PortfolioModel)
admin.site.register(PortfolioItem)
admin.site.register(CopyrightModel)
admin.site.register(FooterIcon)
admin.site.register(FooterModel)
