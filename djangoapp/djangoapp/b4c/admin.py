from django.contrib import admin

from djangoapp.b4c.models import Organization


class OrganizationDisplay(admin.ModelAdmin):
    list_display = ("id", "name", "foundation", "type", "address")
    list_display_links = ("id", "name")
    search_fields = ("name", "address")
    list_filter = ("type",)
    ordering = ("-name",)
    autocomplete_fields = ("members",)
    list_per_page = 10


# Register your models here.
admin.site.register(Organization, OrganizationDisplay)
