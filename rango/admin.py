
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')
    def __init__(self, model: type, admin_site: AdminSite | None) -> None:
        super().__init__(model, admin_site)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
