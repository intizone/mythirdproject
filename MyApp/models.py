from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length = 100)
    details = models.CharField(max_length = 255)
    icon = models.ImageField(upload_to='images/')

class News(models.Model):
    num_of_comments = models.IntegerField(default = 0)
    title = models.CharField(max_length = 70)
    details = models.CharField(max_length = 150)

