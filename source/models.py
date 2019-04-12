from django.db import models


class AnimeModel(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=8)
    mal_id = models.IntegerField(unique=True)
    url = models.URLField()

    start_date = models.DateField()
    end_date = models.DateField()

    episodes = models.IntegerField()
    image_url = models.URLField()
    members = models.IntegerField()
    rank = models.IntegerField()
    score = models.FloatField()

    def __str__(self):
        return f'{self.title}'
