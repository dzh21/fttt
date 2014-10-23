from django.test import TestCase
from tasks42.models import Person, RequestStr
from datetime import date

PERSON1 = Person(
    name="Frodo",
    surname="Baggins",
    date_of_birth=date(1983, 1, 1),
    bio="Hello. My name is Frodo. I was born in...",
    email="frodo@gmail.com",
    jabber="frodo@default.rs",
    skype="frodo",
    other_contacts="phone: +375291111111",
)


class PersonModelTest(TestCase):

    def setUp(self):
        self.person_count = Person.objects.all().count()
        self.person = PERSON1
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


class ViewTest(TestCase):

    def setUp(self):
        self.person = PERSON1
        self.person.save()

    def test_root_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'home.html')

        persons_in_context = response.context['persons']
        self.assertEquals(list(persons_in_context)[-1], self.person)


class RequestModelTest(TestCase):

    def setUp(self):
        self.req = RequestStr()
        self.req.desc = 'http blablabla'
        self.req.save()

    def test_creating_a_new_request_and_save_it(self):
        request_in_db = RequestStr.objects.all()
        self.assertEquals(len(request_in_db), 1)
        self.assertEquals(list(request_in_db)[0], self.req)


