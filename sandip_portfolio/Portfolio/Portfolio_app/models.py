from django.db import models

# Create your models here.
class Projects(models.Model):
    P_name = models.CharField(max_length=255)
    P_descriptions = models.TextField()
    P_image = models.ImageField(upload_to='static/images')

class Feedback(models.Model):
    F_name = models.CharField(max_length=255)
    F_Email = models.EmailField()
    F_mobile = models.CharField(max_length=20)
    F_text=models.TextField(default='')

class Certificate(models.Model):
    C_name = models.CharField(max_length=255)
    C_description = models.TextField()
    C_image = models.ImageField(upload_to='static/image')
    