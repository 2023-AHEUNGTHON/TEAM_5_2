from django.db import models

# Create your models here.

class Wordcloud(models.Model):
    word = models.CharField(max_length=100, primary_key=True, unique=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.word