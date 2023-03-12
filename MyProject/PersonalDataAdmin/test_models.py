from django.test import TestCase
from .models import PersonalData

# Create your tests here.

class PersonalDataTestCase(TestCase):

    def setUp(self):
        PersonalData.objects.create(first_name='Charlie', last_name='Chaplin', date_of_birth='1999-01-02', remarks='nieznośny')

    def test_person_has_last_name(self):
        person = PersonalData.objects.get(last_name='Chaplin')
        self.assertEqual(person.my_name_is(), 'My name is Chaplin')
