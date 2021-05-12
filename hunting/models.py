import uuid
from django.db import models


class Map(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    first_stage = models.ForeignKey('Stage', on_delete=models.CASCADE, blank=True, null=True, help_text='This field has to be set but can be skipped at the beginning if the first stage was not created.')
    date = models.DateTimeField('date published')
    password = models.CharField(max_length=200, help_text='The password to show at the end of the map.')

    def __str__(self):
        return self.title


class Stage(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    answer = models.CharField(max_length=200)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    next_stage = models.ForeignKey('Stage', on_delete=models.PROTECT, blank=True, null=True)
    corresponding_map = models.ForeignKey(Map, on_delete=models.PROTECT, help_text='The corresponding map.')

    def __str__(self):
        return self.question

