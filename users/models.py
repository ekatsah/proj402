from django.db import models
from django.db.models import signals
from django.contrib.auth import models as authmod
from django.contrib.auth.models import User
from django.contrib.auth.management import create_superuser

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    registration = models.IntegerField()
    courses = models.CharField(max_length=30)
 
def create_admin(app, created_models, verbosity, **kwargs):
    try:
        User.objects.get(username='admin')
    except User.DoesNotExist:
        assert User.objects.create_superuser('admin', 'x@x.com', 'test')

signals.post_syncdb.disconnect(create_superuser, sender=authmod,
            dispatch_uid='django.contrib.auth.management.create_superuser')

signals.post_syncdb.connect(create_admin, sender=authmod,
            dispatch_uid='users.models.create_admin')