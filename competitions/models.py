from django.db import models
from uuid import uuid4


class Competitions(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.TextField()
    age_group = models.TextField()
    rank = models.TextField()

    class Meta:
        db_table = 'competitions'


class Competitors(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    competition = models.ForeignKey(Competitions, on_delete=models.CASCADE)
    couple_uuid = models.UUIDField()
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'competitors'


class Referees(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    competition = models.ForeignKey(Competitions, on_delete=models.CASCADE)
    referee_uuid = models.UUIDField()

    class Meta:
        db_table = 'referees'
