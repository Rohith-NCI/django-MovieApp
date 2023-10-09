from django.db import models
  # Create your models here.
class Movie(models.Model):
    # each class variable represents a database i.e. table field in the model
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    genre = models.CharField(max_length=200)
    duration = models.FloatField()
    cover = models.ImageField(upload_to = 'images/')
    
    def __str__(self):
        return self.title + " - " + self.director