from django.contrib import admin
from mediaApp.models import Media
from django.utils.html import format_html


# Register your models here.

class MediaAdmin(admin.ModelAdmin):
    list_display = ("name", "upload_date", "image_tag")
    readonly_fields = ("image_tag",)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;"/>', obj.image.url)
        return ""
    image_tag.short_description = 'Preview'

admin.site.register(Media, MediaAdmin)
