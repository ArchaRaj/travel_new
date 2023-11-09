from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Place2(models.Model):
    name2 = models.CharField(max_length=250)
    img2 = models.ImageField(upload_to='pics2')
    desc2 = models.TextField()

    def __str__(self):
        return self.name2