# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'VotePost'
        db.create_table('upvotes_votepost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('upvotes', ['VotePost'])

        # Adding model 'VoteThread'
        db.create_table('upvotes_votethread', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_question', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_comment', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_rant', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_erratum', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_garbage', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('upvotes', ['VoteThread'])

        # Adding model 'VoteDocument'
        db.create_table('upvotes_votedocument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(default='O', max_length=1)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_reference', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_support', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_summary', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_exam', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_project', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_solution', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cat_others', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('upvotes', ['VoteDocument'])

        # Adding model 'VoteHistory'
        db.create_table('upvotes_votehistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('ressource', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('resid', self.gf('django.db.models.fields.IntegerField')()),
            ('cat', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('upvotes', ['VoteHistory'])

        # Adding unique constraint on 'VoteHistory', fields ['voter', 'ressource', 'resid']
        db.create_unique('upvotes_votehistory', ['voter_id', 'ressource', 'resid'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'VoteHistory', fields ['voter', 'ressource', 'resid']
        db.delete_unique('upvotes_votehistory', ['voter_id', 'ressource', 'resid'])

        # Deleting model 'VotePost'
        db.delete_table('upvotes_votepost')

        # Deleting model 'VoteThread'
        db.delete_table('upvotes_votethread')

        # Deleting model 'VoteDocument'
        db.delete_table('upvotes_votedocument')

        # Deleting model 'VoteHistory'
        db.delete_table('upvotes_votehistory')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 2, 20, 48, 37, 257306)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 2, 20, 48, 37, 257255)'}),
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
        'upvotes.votedocument': {
            'Meta': {'object_name': 'VoteDocument'},
            'cat_exam': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_others': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_project': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_reference': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_solution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_summary': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_support': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'upvotes.votehistory': {
            'Meta': {'unique_together': "(('voter', 'ressource', 'resid'),)", 'object_name': 'VoteHistory'},
            'cat': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resid': ('django.db.models.fields.IntegerField', [], {}),
            'ressource': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'upvotes.votepost': {
            'Meta': {'object_name': 'VotePost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        'upvotes.votethread': {
            'Meta': {'object_name': 'VoteThread'},
            'cat_comment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_erratum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_garbage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_question': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_rant': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['upvotes']
