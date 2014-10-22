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
        self.assertEquals(first_person_in_db.date_of_birth,
            person.date_of_birth)
        self.assertEquals(first_person_in_db.bio, person.bio)
        self.assertEquals(first_person_in_db.email, person.email)
        self.assertEquals(first_person_in_db.jabber, person.jabber)
        self.assertEquals(first_person_in_db.skype, person.skype)
        self.assertEquals(first_person_in_db.other_contacts,
            person.other_contacts)


class ViewTest(TestCase):
    def test_root_url(self):
        person = Person()
        person.name = "Evhen"
        person.surname = "Davliud"
        person.date_of_birth = "1983-07-21"
        person.bio = """
            I was born in Lubetch Chernigov region Ukrain.
        """
        person.email = "dzh21@tut.by"
        person.jabber = "dzh@default.rs"
        person.skype = "dzha21"
        person.other_contacts = "phone +375297602862"
        person.save()

        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'home.html')

        person_in_context = response.context['person']
        self.assertEquals(person_in_context, person)
