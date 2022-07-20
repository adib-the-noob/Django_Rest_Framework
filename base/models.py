from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)
