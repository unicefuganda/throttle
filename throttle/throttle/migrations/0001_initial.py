# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KannelMessage'
        db.create_table(u'throttle_kannelmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('backend', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'throttle', ['KannelMessage'])


    def backwards(self, orm):
        # Deleting model 'KannelMessage'
        db.delete_table(u'throttle_kannelmessage')


    models = {
        u'throttle.kannelmessage': {
            'Meta': {'ordering': "['-created']", 'object_name': 'KannelMessage'},
            'backend': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['throttle']