# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RequestObject.save_date_time'
        db.delete_column(u'tasks42_requestobject', 'save_date_time')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'RequestObject.save_date_time'
        raise RuntimeError("Cannot reverse this migration. 'RequestObject.save_date_time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RequestObject.save_date_time'
        db.add_column(u'tasks42_requestobject', 'save_date_time',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)


    models = {
        u'tasks42.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tasks42.requestobject': {
            'Meta': {'object_name': 'RequestObject'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tasks42']