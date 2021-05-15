import uuid
from django.db import models
from django.utils import timezone


class Map(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=200, help_text='The password to show at the end of the map.')

    def __str__(self):
        return self.title


class Stage(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    answer = models.CharField(max_length=200)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.PositiveIntegerField(help_text='The stages are sorted by their level, so the level with the next higher number will be the next question. First question is the lowest index.')
    corresponding_map = models.ForeignKey(Map, related_name='stages', on_delete=models.PROTECT, help_text='The corresponding map.')

    class Meta:
        ordering = ['level']

    def is_latest(self):
        ''' Check whether this function has the highest level, which makes it the last question. '''
        return Stage.objects.last() == self

    def __str__(self):
        return self.question

