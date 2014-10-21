from django.test import TestCase
from tasks.models import Person
from datetime import date


class PersonModelTest(TestCase):

    def test_creating_a_new_person_and_saving_it(self):
        person = Person()
        person.name = "Frodo"
        person.surname = "Baggins"
        person.date_of_birth = date(1983, 1, 1)
        person.bio = "Hello. My name is Frodo. I was born in..."
        person.email = "frodo@gmail.com"
        person.jabber = "frodo@default.rs"
        person.skype = "frodo"
        person.other_contacts = "phone: +375291111111"

        person.save()

        all_persons_in_db = Person.objects.all()
        self.assertEquals(len(all_persons_in_db), 1)
        first_person_in_db = all_persons_in_db[0]
        self.assertEquals(first_person_in_db, person)

        self.assertEquals(first_person_in_db.name, person.name)
        self.assertEquals(first_person_in_db.surname, person.surname)


