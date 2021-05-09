from django.db import models

# Create your models here.
class Author(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)


class Books(models.Model):
    tittle=models.CharField(max_length=20)
    ratings=models.CharField(max_length=10)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')    

def __str__(self) :
    return self.FirstName
        
    