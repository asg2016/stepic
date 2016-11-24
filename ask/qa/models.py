from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True,default=now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', default=1)
    likes = models.ManyToManyField(User, related_name='question_likes', default=0)
    objects = QuestionManager()
    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})

    def __unicode__(self):
        return self.title
    class Meta:
        db_table = 'Question'

class QuestionManager(models.Manager):
    def new(self):
        return self.filter(added_at=now())
    def popular(self):
        return self.orderby('rating')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True,default=now())
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1, null=True)
    class Meta:
        db_table = 'Answer'
