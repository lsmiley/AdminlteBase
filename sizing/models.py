from django.db import models
from django.contrib.auth.models import User


class Sizing(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    owner = models.CharField(max_length=300, blank=True)
    note = models.TextField(blank=True)
    created_by = models.ForeignKey(User,
        related_name="sizings", blank=True, null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class SizingItem(models.Model):
    """
    A Class for Sizings items.

    """
    sizing = models.ForeignKey(Sizing, related_name="has_items", on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Item")
    language = models.CharField(max_length=3)

