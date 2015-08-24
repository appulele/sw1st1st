# -*- coding: utf-8 -*-
from django.db import models

class Person(models.Model):
    
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


 
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')