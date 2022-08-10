from django.db import models

class Phone_book(models.Model):
    name = models.CharField('Name', max_length=200)
    value = models.PositiveBigIntegerField('Phone number')
