from django.test import TestCase
from tasks42.models import Person
from datetime import date


class PersonModelTest(TestCase):

    def setUp(self):
        self.person_count = Person.objects.all().count()
        self.person = Person(
            name="Frodo",
            surname="Baggins",
            date_of_birth=date(1983, 1, 1),
            bio="Hello. My name is Frodo. I was born in...",
            email="frodo@gmail.com",
            jabber="frodo@default.rs",
            skype="frodo",
            other_contacts="phone: +375291111111",
        )
        self.person.save()

    def test_creating_a_new_person_and_saving_it(self):
        all_persons_in_db = Person.objects.all()
        self.assertEquals(len(all_persons_in_db), self.person_count + 1)

        last_person_in_db = list(all_persons_in_db)[-1]
        self.assertEquals(last_person_in_db, self.person)

        self.assertEquals(last_person_in_db.name, self.person.name)
        self.assertEquals(last_person_in_db.surname, self.person.surname)
        self.assertEquals(last_person_in_db.date_of_birth,
            self.person.date_of_birth)
        self.assertEquals(last_person_in_db.bio, self.person.bio)
        self.assertEquals(last_person_in_db.email, self.person.email)
        self.assertEquals(last_person_in_db.jabber, self.person.jabber)
        self.assertEquals(last_person_in_db.skype, self.person.skype)
        self.assertEquals(last_person_in_db.other_contacts,
            self.person.other_contacts)


class PersonViewTest(TestCase):

    def setUp(self):
        self.me = Person(
            name="Evhen",
            surname="Davliud",
            date_of_birth=date(1983, 7, 21),
            bio="I was born in Lubetch Chernigov region Ukraine. In 1995 moved to Belarus. In 2001-2006 studied in The Belarusian State University of Informatics and Radioelectronics.",
            email="dzh21@tut.by",
            jabber="dzh@default.rs",
            skype="dzha21",
            other_contacts="phone +375297602862",
        )

    def test_root_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'home.html')

        persons_in_context = response.context['persons']

        self.assertEquals(persons_in_context[0].name, self.me.name)
        self.assertEquals(persons_in_context[0].surname, self.me.surname)
        self.assertEquals(
            persons_in_context[0].date_of_birth,
            self.me.date_of_birth
        )
        self.assertEquals(persons_in_context[0].bio, self.me.bio)
        self.assertEquals(persons_in_context[0].email, self.me.email)
        self.assertEquals(persons_in_context[0].jabber, self.me.jabber)
        self.assertEquals(persons_in_context[0].skype, self.me.skype)
        self.assertEquals(
            persons_in_context[0].other_contacts,
            self.me.other_contacts
        )

        self.assertIn(self.me.name, response.content)
        self.assertIn(self.me.surname, response.content)
        self.assertIn(
            self.me.date_of_birth.strftime('%B %d, %Y'),
            response.content
            )
        self.assertIn(self.me.bio, response.content)
        self.assertIn(self.me.email, response.content)
        self.assertIn(self.me.jabber, response.content)
        self.assertIn(self.me.skype, response.content)
        self.assertIn(self.me.other_contacts, response.content)
