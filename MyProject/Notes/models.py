from django.db import models

# Create your models here.

class Note(models.Model):
    '''reprezentuje notatkę'''
    title = models.CharField(max_length=50)
    note = models.TextField()
    create_date = models.DateTimeField()
    category = models.ForeignKey('Notes.Category', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}, {self.category}, {self.create_date}'

    class Meta:
        verbose_name = "Notatka"
        verbose_name_plural = "Notatki"

class Category(models.Model):
    '''reprezentuje kategorię notatki'''
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'
