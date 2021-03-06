# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'KannelMessage.handled'
        db.add_column(u'throttle_kannelmessage', 'handled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'KannelMessage.handled'
        db.delete_column(u'throttle_kannelmessage', 'handled')


    models = {
        u'throttle.kannelmessage': {
            'Meta': {'ordering': "['-created']", 'object_name': 'KannelMessage'},
            'backend': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'handled': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['throttle']