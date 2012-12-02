# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Criterion'
        db.create_table('team360_criterion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('team360', ['Criterion'])

        # Adding model 'WeekCriterion'
        db.create_table('team360_weekcriterion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('criterion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team360.Criterion'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('team360', ['WeekCriterion'])

        # Adding model 'WeekRater'
        db.create_table('team360_weekrater', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rater', self.gf('django.db.models.fields.related.ForeignKey')(related_name='weekrater_rater', to=orm['auth.User'])),
            ('rated', self.gf('django.db.models.fields.related.ForeignKey')(related_name='weekrater_rated', to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('team360', ['WeekRater'])

        # Adding model 'Rating'
        db.create_table('team360_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('criterion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team360.Criterion'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('rater', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rating_rater', to=orm['auth.User'])),
            ('rated', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rating_rated', to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('team360', ['Rating'])


    def backwards(self, orm):
        # Deleting model 'Criterion'
        db.delete_table('team360_criterion')

        # Deleting model 'WeekCriterion'
        db.delete_table('team360_weekcriterion')

        # Deleting model 'WeekRater'
        db.delete_table('team360_weekrater')

        # Deleting model 'Rating'
        db.delete_table('team360_rating')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'team360.criterion': {
            'Meta': {'object_name': 'Criterion'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'team360.rating': {
            'Meta': {'object_name': 'Rating'},
            'criterion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team360.Criterion']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rated': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rating_rated'", 'to': "orm['auth.User']"}),
            'rater': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rating_rater'", 'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'team360.weekcriterion': {
            'Meta': {'object_name': 'WeekCriterion'},
            'criterion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team360.Criterion']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'team360.weekrater': {
            'Meta': {'object_name': 'WeekRater'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rated': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'weekrater_rated'", 'to': "orm['auth.User']"}),
            'rater': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'weekrater_rater'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['team360']