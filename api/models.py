from django.db import models

# Create your models here.
# Author models stores book authour infomation
class Author(models.Model):
    name = models.CharField(max_length=100) # author name 

    def __str__(self):
        return self.name
    

# Book model store book data with a link to author 

class Book(models.Model):
    title = models.CharField(max_length=200) # Book title
    publication_year = models.IntegerField()  # year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) # link to author


    def __str__(self):
        return self.title

