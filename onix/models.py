from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Unity(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120)
    number = models.IntegerField(verbose_name='Unity', unique=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    level = models.IntegerField(default=1, verbose_name='Level')

    class Meta:
        db_table = 'unity'

    def __str__(self):
        return self.name

    def get_lessons(self):
        return Lesson.objects.filter(unity=self).prefetch_related('results')


class Answer(models.Model):
    name = models.CharField(verbose_name='Answer', max_length=255)
    extra = models.CharField(verbose_name='Other answer', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return "{0} - {1}".format(self.name, self.extra)


class Lesson(models.Model):
    name = models.CharField(verbose_name='Name', max_length=40)
    unity = models.ForeignKey(Unity, verbose_name='Unity', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    class Meta:
        db_table = 'lesson'

    def __str__(self):
        return "Unity: {0} - Lesson: {1}".format(self.unity.name, self.name)


class Media(models.Model):
    name = models.CharField(verbose_name='Name', max_length=40)
    url = models.URLField(verbose_name='URL')

    class Meta:
        db_table = 'media'

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.TextField(verbose_name='Question')
    answers = models.ManyToManyField(Answer, related_name='answers', db_table='question_has_answer', default=None,
                                     null=True, blank=True)
    answer_correct = models.ForeignKey(Answer, verbose_name='Correct answer')
    lesson = models.ForeignKey(Lesson, verbose_name=u'Lesson', related_name='questions')
    audio = models.ForeignKey(Media, related_name='audio', blank=True, null=True, on_delete=models. DO_NOTHING)
    image = models.ForeignKey(Media, related_name='image', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.name


class Result(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.DO_NOTHING)
    lesson = models.ForeignKey(Lesson, related_name='results', verbose_name='Lesson', on_delete=models.DO_NOTHING)
    finished_at = models.DateTimeField(default=datetime.now, verbose_name='Finished at')
    question = models.ForeignKey(Question, related_name='questions', verbose_name='Question', on_delete=models.DO_NOTHING)
    correct = models.BooleanField()

    class Meta:
        db_table = 'result'

    def __str__(self):
        return self.user.username
