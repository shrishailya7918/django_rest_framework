from django.db import models

class CelebrityTable(models.Model):
    name = models.CharField(max_length=20)
    recent_released_movie = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return  self.name