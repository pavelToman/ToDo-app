from django.db import models
from django.utils import timezone
# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='notes')
    text = models.CharField(max_length=1024, blank=True)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self) -> str:
        return "{} | [{}]".format(self.text, "✓" if self.done else " ")