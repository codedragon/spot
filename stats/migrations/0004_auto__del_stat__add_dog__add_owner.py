# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Stat'
        db.delete_table(u'stats_stat')

        # Adding model 'Dog'
        db.create_table(u'stats_dog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dog_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Owner'])),
        ))
        db.send_create_signal(u'stats', ['Dog'])

        # Adding model 'Owner'
        db.create_table(u'stats_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'stats', ['Owner'])


    def backwards(self, orm):
        # Adding model 'Stat'
        db.create_table(u'stats_stat', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dog_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'stats', ['Stat'])

        # Deleting model 'Dog'
        db.delete_table(u'stats_dog')

        # Deleting model 'Owner'
        db.delete_table(u'stats_owner')


    models = {
        u'stats.dog': {
            'Meta': {'object_name': 'Dog'},
            'dog_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Owner']"})
        },
        u'stats.owner': {
            'Meta': {'object_name': 'Owner'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['stats']