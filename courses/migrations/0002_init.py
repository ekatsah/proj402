# encoding: utf-8
from south.v2 import DataMigration

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        genie = orm["courses.course"].objects.create(slug='info-f-307', name='Génie logiciel et management des projets');
        compilo = orm["courses.course"].objects.create(slug='info-f-403', name='Introduction to Language Theory and Compilation');
        secu = orm["courses.course"].objects.create(slug='info-f-405', name='Computer security');
        competcomp = orm["courses.course"].objects.create(slug='info-f-408', name='Computability and complexity');
        learning_dynamic = orm["courses.course"].objects.create(slug='info-f-409', name='Learning dynamics');
        ml = orm["courses.course"].objects.create(slug='info-f-422', name='Statistical foundations of machine learning');
        crypto = orm["courses.course"].objects.create(slug='info-f-514', name='Protocols, cryptanalysis and mathematical cryptology');
        coding_theory = orm["courses.course"].objects.create(slug='info-h-300', name='Information and coding theory');
        tech_of_ai = orm["courses.course"].objects.create(slug='info-h-410', name='Techniques of artificial intelligence');
        optimisation = orm["courses.course"].objects.create(slug='info-h-413', name='Heuristic optimisation');
        swarm = orm["courses.course"].objects.create(slug='info-h-414', name='Swarm Intelligence');
        xml = orm["courses.course"].objects.create(slug='info-h-509', name='XML Technologies');
        rechop = orm["courses.course"].objects.create(slug='math-h-404', name='Operational research');
        comp_project = orm["courses.course"].objects.create(slug='proj-h-402', name='Computing project');

        discussion = orm["courses.course"].objects.create(slug='402-discussions', name='General discussion about project 402');
        bts = orm["courses.course"].objects.create(slug='402-bugs', name='Bug tracking of project 402');

        root = orm["courses.category"].objects.create(name='ROOT', description='root of the category tree');

        bio = orm["courses.category"].objects.create(name='Biology', description='BA-BIOL, BA-IRBI, MA-BMOL...');
        chemistry = orm["courses.category"].objects.create(name='Chemistry', description='BA-CHIM, MA-CHIM');
        geography = orm["courses.category"].objects.create(name='Geography', description='BA-GEOG');
        geology = orm["courses.category"].objects.create(name='Geology', description='BA-GEOL');
        computing = orm["courses.category"].objects.create(name='Computing', description='BA-INFO, MA-INFO');
        maths = orm["courses.category"].objects.create(name='Maths', description='BA-MATH, MA-MATH');
        physics = orm["courses.category"].objects.create(name='Physics', description='BA-PHYS, MA-PHYS');

        bainfo1 = orm["courses.category"].objects.create(name='BA-INFO1', description='First year in computer science');
        bainfo2 = orm["courses.category"].objects.create(name='BA-INFO2', description='Second year in computer science');
        bainfo3 = orm["courses.category"].objects.create(name='BA-INFO3', description='Third year in computer science');
        mainfo1 = orm["courses.category"].objects.create(name='MA-INFO1', description='First year of the master in computer science');

        ai = orm["courses.category"].objects.create(name='Artificial Intelligence', description='IA stuff and topics');
        algoopt = orm["courses.category"].objects.create(name='Algorithm Optimisation', description='Mega mathematical brain needed');
        beerd = orm["courses.category"].objects.create(name='Beer drinking', description='Ballmer peak related things');

        root.holds.add(bio)
        root.holds.add(chemistry)
        root.holds.add(geography)
        root.holds.add(geology)
        root.holds.add(computing)
        root.holds.add(maths)
        root.holds.add(physics)
        root.save()

        computing.holds.add(bainfo1)
        computing.holds.add(bainfo2)
        computing.holds.add(bainfo3)
        computing.holds.add(mainfo1)
        computing.save()

        mainfo1.holds.add(ai)
        mainfo1.holds.add(algoopt)
        mainfo1.holds.add(beerd)

        mainfo1.contains.add(genie)
        mainfo1.contains.add(compilo)
        mainfo1.contains.add(secu)
        mainfo1.contains.add(competcomp)
        mainfo1.contains.add(crypto)
        mainfo1.contains.add(coding_theory)
        mainfo1.contains.add(xml)
        mainfo1.contains.add(rechop)
        mainfo1.contains.add(comp_project)
        mainfo1.save()

        ai.contains.add(learning_dynamic)
        ai.contains.add(ml)
        ai.contains.add(tech_of_ai)
        ai.contains.add(optimisation)
        ai.contains.add(swarm)
        ai.save()

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
