from django.db import models
from django.contrib.auth.models import User

CAT_THREADS = (
    ('Q', 'Question'),
    ('C', 'Comment'),
    ('R', 'Rant'),
    ('E', 'Erratum'),
    ('G', 'Garbage'),
)

# This is duplicated in upvotes.url and course_show JS                                   
CAT_DOCUMENTS = (
    ('R', 'Reference'),
    ('O', 'Official Support'),
    ('S', 'Summary'),
    ('E', 'Old Exam'),
    ('P', 'Old Project'),
    ('L', 'Old Solutions'),
    ('D', 'Others'),
)

RESSOURCES = (
    ('D', 'Document'),
    ('T', 'Thread'),
    ('P', 'Post'),
)

class VotePost(models.Model):
    score = models.IntegerField(null=False)

class VoteThread(models.Model):
    category = models.CharField(max_length=1, choices=CAT_THREADS)
    score = models.IntegerField(null=False, default=0)

    cat_question = models.IntegerField(null=False, default=0)
    cat_comment = models.IntegerField(null=False, default=0)
    cat_rant = models.IntegerField(null=False, default=0)
    cat_erratum = models.IntegerField(null=False, default=0)
    cat_garbage = models.IntegerField(null=False, default=0)

class VoteDocument(models.Model):
    category = models.CharField(max_length=1, choices=CAT_DOCUMENTS, default="O")
    score = models.IntegerField(null=False, default=0)
    
    cat_reference = models.IntegerField(null=False, default=0)
    cat_support = models.IntegerField(null=False, default=0)
    cat_summary = models.IntegerField(null=False, default=0)
    cat_exam = models.IntegerField(null=False, default=0)
    cat_project = models.IntegerField(null=False, default=0)
    cat_solution = models.IntegerField(null=False, default=0)
    cat_others = models.IntegerField(null=False, default=0)

    def full_category(self):
        return [ v for k, v in CAT_DOCUMENTS if k == self.category ][0]

class VoteHistory(models.Model):
    voter = models.ForeignKey(User)
    ressource = models.CharField(max_length=1, choices=RESSOURCES)
    resid = models.IntegerField(null=False)
    cat = models.CharField(max_length=1, null=True)
    score = models.IntegerField(null=False)

    class Meta:
        unique_together = ('voter', 'ressource', 'resid')
