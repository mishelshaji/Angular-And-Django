from django.db import models

class Movie(models.Model):

    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        verbose_name="MovieName",
        max_length= 200,
        blank=False,
        null= False,
    )

    director = models.CharField(
        verbose_name="Director",
        max_length= 100,
        blank=False,
    )

    description =models.TextField(
        verbose_name= "Descrtiptions",
        blank=False,
        null= False,
    ) 
    
    release_date = models.DateField(
        verbose_name= "Release Date",
        blank=False,
        null=False
    )

    added_date = models.DateField(
        auto_now_add=True,
    )

    
    updated_on = models.DateField(
        auto_now=True,
    )
    