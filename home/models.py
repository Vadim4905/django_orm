from django.db import models
 
# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre,related_name='games')
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3,decimal_places=2)
    
    def __str__(self):
        return self.title
    
