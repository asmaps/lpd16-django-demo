from django.db import models


class Presenter(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Presentation(models.Model):
    title = models.CharField(max_length=200)
    presenter = models.ForeignKey('lpd.Presenter')
    length = models.PositiveIntegerField(default=60)

    def __str__(self):
        return self.title
