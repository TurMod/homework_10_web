from django.db import models

# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=30, null=False, unique=True)
    biography = models.TextField()

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
