from django.db import models

# Create your models here.
class Instructors(models.Model):
    instructor_name = models.CharField(max_length=100)
    instructor_designation = models.CharField(max_length=100)
    instructor_image = models.ImageField(upload_to='instructor_images/')


    def __str__(self):
        return self.instructor_name