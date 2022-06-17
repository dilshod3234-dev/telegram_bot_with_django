from django.db import models

from django.db import models
from django.db.models import CASCADE, Model
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('app.Category', CASCADE)

    def __str__(self):
        return self.name
