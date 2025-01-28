from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=64, blank=False, primary_key=True)
    image = models.ImageField(upload_to='', default="images.png" ,blank=True)
    bio = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=200, blank=True)
    DOB = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.username} : {self.name}"

class Post(models.Model):
    username = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = '', blank=True)
    content = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return f"{self.username} : {self.content}"

