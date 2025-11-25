from django.contrib import admin
from contactApp.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",  "subject", "message", "created_at")
    

admin.site.register(Contact, ContactAdmin)
