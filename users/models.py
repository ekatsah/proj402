from random import choice
from string import printable
from django.db import models
from django.db.models import signals
from django.contrib.auth import models as authmod
from django.contrib.auth.models import User
from django.contrib.auth.management import create_superuser
from courses.models import Course

class CourseFollow(models.Model):
    course = models.ForeignKey(Course)
    last_visit = models.DateTimeField(auto_now_add=True, null=False)
    visited = models.IntegerField(default=0, null=False)
    # FIXME do we need unique on user:course ?

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    registration = models.CharField(max_length=80, null=True)
    section = models.CharField(max_length=80, null=True)
    courses = models.ManyToManyField(CourseFollow)
    welcome = models.BooleanField(default=True)
    moderate = models.BooleanField(default=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_admin(app, created_models, verbosity, **kwargs):
    try:
        User.objects.get(username='admin')
    except User.DoesNotExist:
        rpwd = ''.join(choice(printable) for x in xrange(100))
        assert User.objects.create_superuser('admin', 'x@x.com', rpwd)

signals.post_syncdb.disconnect(create_superuser, sender=authmod,
            dispatch_uid='django.contrib.auth.management.create_superuser')

signals.post_syncdb.connect(create_admin, sender=authmod,
            dispatch_uid='users.models.create_admin')