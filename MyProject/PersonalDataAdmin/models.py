from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.

GENDER = (('m', 'male'),('f','female'), ('u','unspecified'))

class PersonalData(models.Model):
    '''reprezentuje osobę'''
    gender = models.CharField(max_length=10, choices=GENDER, default='m')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()
    remarks = models.TextField(default='aktualnie brak')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.date_of_birth}'

    def my_name_is(self):
        return f'My name is {self.last_name}'

    def get_student(self):
        '''na obj.PersonalData'''
        try:
            self.student
        except ObjectDoesNotExist:
            print('objekt nie jest studentem')


    class Meta:
        verbose_name='Osoba'
        verbose_name_plural='Osoby'

class Student(models.Model):
    """reprezentuje studenta; osoba nie musi być studentem, student musi być osobą; jest w realcji z osobą
    OneToOne"""
    index_numb = models.PositiveIntegerField(unique=True)
    immatr_date = models.DateTimeField()
    dekan_remarks = models.TextField(default='aktualnie brak')
    person_id = models.OneToOneField('PersonalDataAdmin.PersonalData', on_delete=models.PROTECT)
    course = models.ForeignKey('PersonalDataAdmin.Course', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.person_id}, {self.index_numb}, {self.immatr_date}'

    class Meta:
        verbose_name='Student'
        verbose_name_plural='Studenci'

class Course(models.Model):
    '''reprezentacja kierunków studiów
    na jednym kierunku może studiować wielu studentów
    jeden student może studiować na jednym kierunku'''
    course = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.course}'

    class Meta:
        verbose_name='Kierunek studiów'
        verbose_name_plural='Kierunki studiów'





