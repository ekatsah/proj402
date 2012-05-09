# encoding: utf-8
from south.v2 import DataMigration

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        discussion = orm["courses.course"].objects.create(slug='402-discussions', name='General discussion about project 402');
        bts = orm["courses.course"].objects.create(slug='402-bugs', name='Bug tracking of project 402');
        root = orm["courses.category"].objects.create(name='ROOT', description='Zoidberg root tree of life');
        zoidberg = orm["courses.category"].objects.create(name='Project 402', description='Zoidberg release');
        zoidberg.contains.add(discussion)
        zoidberg.contains.add(bts)
        zoidberg.save()


    def backwards(self, orm):
        "Write your backwards methods here."


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 3, 0, 22, 10, 399928)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 3, 0, 22, 10, 399874)'}),
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
        'courses.category': {
            'Meta': {'object_name': 'Category'},
            'contains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['courses.Course']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'holds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['courses.Category']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Document']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['messages.Thread']", 'symmetrical': 'False'})
        },
        'documents.document': {
            'Meta': {'object_name': 'Document'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'done': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Page']", 'symmetrical': 'False'}),
            'points': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['upvotes.VoteDocument']"}),
            'ready': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'refer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_course'", 'to': "orm['courses.Course']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['messages.Thread']", 'symmetrical': 'False'}),
            'words': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
        },
        'documents.page': {
            'Meta': {'object_name': 'Page'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['messages.Thread']", 'symmetrical': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'messages.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['messages.Message']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['messages.Thread']"})
        },
        'messages.thread': {
            'Meta': {'object_name': 'Thread'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msgs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'back_thread'", 'symmetrical': 'False', 'to': "orm['messages.Message']"}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'referc': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_tcourse'", 'null': 'True', 'to': "orm['courses.Course']"}),
            'referd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_tdoc'", 'null': 'True', 'to': "orm['documents.Document']"}),
            'referp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_tpage'", 'null': 'True', 'to': "orm['documents.Page']"}),
            'subject': ('django.db.models.fields.TextField', [], {})
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
        }
    }

    complete_apps = ['courses']
