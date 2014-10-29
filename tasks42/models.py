from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50)
    other_contacts = models.TextField()

    def __unicode__(self):
        return self.name + ' ' + self.surname


class RequestObject(models.Model):
    desc = models.TextField()
    save_date_time = models.DateTimeField(default=timezone.now)
    remote_address = models.CharField(max_length=20, default='localhost')

    def __unicode__(self):
        return "Request #" + str(self.id)

