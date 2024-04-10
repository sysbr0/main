from django.db import models

class Book(models.Model):
    element_id = models.CharField(max_length=100)
    neo4j_id = models.IntegerField()
    avg_age = models.IntegerField()
    avg_book_rating = models.FloatField()
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    image_url = models.URLField()
    publisher = models.CharField(max_length=100)
    year_of_publication = models.IntegerField()
    category_id = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()
