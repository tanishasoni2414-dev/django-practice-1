from django.db import models

# Create your models here.
class Courses(models.Model):
    rating = models.FloatField()
    duration = models.CharField(max_length=50)
    course_name = models.CharField(max_length=200)
    course_price = models.FloatField()
    students_enrolled = models.IntegerField()
    course_image = models.ImageField(upload_to='course_images/')
    instructor_name = models.CharField(max_length=100)
    # join_now = models.URLField()
    # read_more = models.URLField()