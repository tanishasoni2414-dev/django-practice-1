from django.contrib import admin
from addCourses.models import Courses

# Register your models here.
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'instructor_name', 'rating', 'course_price', 'students_enrolled', 'duration', 'course_image')
    # field = "__all__"
admin.site.register(Courses, CoursesAdmin)