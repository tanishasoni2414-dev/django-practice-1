from django.contrib import admin
from addInstructors.models import Instructors
# Register your models here.
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('instructor_name', 'instructor_designation', 'instructor_image')    
    
admin.site.register(Instructors, InstructorsAdmin)