from django.db import models
from django.utils.translation import gettext as _
# from django.contrib.postgres.indexes import GINIndex
# Create your models here.

class Book(models.Model):
    title = models.CharField(_("title"), max_length=1000, null=False, db_index=True)
    authors = models.CharField(_("authors"), max_length=1000)
    
    # class Meta:
    #     indexes = [
    #         GINIndex(name='NewGinIndex', fields=['title'])
    #     ]
    def __str__(self):
        return self.title