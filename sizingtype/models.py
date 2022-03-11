from django.db import models
from ckeditor.fields import RichTextField


class Sizingtype(models.Model):
    Sizingtypename = models.CharField(
        db_column='Sizingtypename',
        max_length=150,
        blank=True,
        null=True)
    Sizingtypedesc = models.CharField(
        db_column='Sizingtypedesc',
        max_length=150,
        blank=True,
        null=True)
    Sizingtypetype = models.CharField(
        db_column='Sizingtype',
        max_length=150,
        blank=True,
        null=True)
    memo = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.Sizingtypename
