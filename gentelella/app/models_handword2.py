# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Chapter(models.Model):
    id = models.IntegerField(primary_key=True)
    subjectid = models.IntegerField(db_column='subjectId', blank=True, null=True)  # Field name made lowercase.
    pharseid = models.IntegerField(db_column='pharseId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='gradeId', blank=True, null=True)  # Field name made lowercase.
    editionid = models.IntegerField(db_column='editionId', blank=True, null=True)  # Field name made lowercase.
    chapter = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    section = models.CharField(max_length=255, blank=True, null=True)
    knowledgeid = models.IntegerField(db_column='knowledgeId', blank=True, null=True)  # Field name made lowercase.
    chapterorder = models.IntegerField(db_column='chapterOrder', blank=True, null=True)  # Field name made lowercase.
    unitorder = models.IntegerField(db_column='unitOrder', blank=True, null=True)  # Field name made lowercase.
    sectionorder = models.IntegerField(db_column='sectionOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chapter'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Edition(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'edition'


class Grade(models.Model):
    gradeid = models.IntegerField(db_column='gradeId', primary_key=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='gradeName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grade'

class Papertype(models.Model):
    papertypeid = models.IntegerField(db_column='papertypeid', primary_key=True)  # Field name made lowercase.
    papertypename = models.CharField(db_column='papertypename', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'papertype'


class KnowledgeBasic(models.Model):
    knowledgename = models.CharField(db_column='knowledgeName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='subjectId', blank=True, null=True)  # Field name made lowercase.
    pharseid = models.IntegerField(db_column='pharseId', blank=True, null=True)  # Field name made lowercase.
    key = models.CharField(max_length=500, blank=True, null=True)
    descs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledge_basic'


class KnowledgeLevel(models.Model):
    subjectid = models.IntegerField(db_column='subjectId', blank=True, null=True)  # Field name made lowercase.
    pharseid = models.IntegerField(db_column='pharseId', blank=True, null=True)  # Field name made lowercase.
    knowledge_level_1 = models.IntegerField(blank=True, null=True)
    knowledge_level_2 = models.IntegerField(blank=True, null=True)
    knowledge_level_3 = models.IntegerField(blank=True, null=True)
    knowledgeid = models.IntegerField(db_column='knowledgeId', blank=True, null=True)  # Field name made lowercase.
    level1 = models.CharField(max_length=100, blank=True, null=True)
    level2 = models.CharField(max_length=100, blank=True, null=True)
    level3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledge_level'


class Pharse(models.Model):
    pharseid = models.IntegerField(db_column='pharseId', primary_key=True)  # Field name made lowercase.
    pharsename = models.CharField(db_column='pharseName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pharse'


class Pharsegrade(models.Model):
    pharseid = models.IntegerField(db_column='pharseId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.CharField(db_column='gradeId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pharsegrade'


class QuestionKnowledgeBasicId(models.Model):
    knowledge_basic_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_knowledge_basic_id'


class Questions(models.Model):
    title = models.TextField(blank=True, null=True)
    option_a = models.TextField(blank=True, null=True)
    option_b = models.TextField(blank=True, null=True)
    option_c = models.TextField(blank=True, null=True)
    option_d = models.TextField(blank=True, null=True)
    option_e = models.TextField(blank=True, null=True)
    answer1 = models.TextField(blank=True, null=True)
    answer2 = models.TextField(blank=True, null=True)
    parse = models.TextField(blank=True, null=True)
    qtpye = models.CharField(max_length=80, blank=True, null=True)
    diff = models.FloatField(blank=True, null=True)
    md5 = models.CharField(max_length=50, blank=True, null=True)
    subjectid = models.IntegerField(db_column='subjectId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='gradeId', blank=True, null=True)  # Field name made lowercase.
    knowledges = models.CharField(max_length=200, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    papertpye = models.CharField(db_column='paperTpye', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=200, blank=True, null=True)
    fromsite = models.CharField(db_column='fromSite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issub = models.IntegerField(db_column='isSub', blank=True, null=True)  # Field name made lowercase.
    isnormal = models.IntegerField(db_column='isNormal', blank=True, null=True)  # Field name made lowercase.
    iskonw = models.IntegerField(db_column='isKonw', blank=True, null=True)  # Field name made lowercase.
    tiid = models.CharField(max_length=50, blank=True, null=True)
    similarity = models.IntegerField(db_column='Similarity', blank=True, null=True)  # Field name made lowercase.
    isunique = models.IntegerField(blank=True, null=True)
    md52 = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'
        unique_together = (('fromsite', 'tiid'),)


class Subject(models.Model):
    subjectid = models.IntegerField(db_column='subjectId', primary_key=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='subjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pinyin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'


class Subquestion(models.Model):
    title = models.TextField(blank=True, null=True)
    option_a = models.TextField(blank=True, null=True)
    option_b = models.TextField(blank=True, null=True)
    option_c = models.TextField(blank=True, null=True)
    option_d = models.TextField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    answer1 = models.TextField(blank=True, null=True)
    answer2 = models.TextField(blank=True, null=True)
    parse = models.TextField(blank=True, null=True)
    qtpye = models.CharField(max_length=80, blank=True, null=True)
    diff = models.FloatField(blank=True, null=True)
    subjectid = models.IntegerField(db_column='subjectId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='gradeId', blank=True, null=True)  # Field name made lowercase.
    knowledges = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    tiid = models.CharField(max_length=50, blank=True, null=True)
    ptiid = models.CharField(max_length=50, blank=True, null=True)
    fromsite = models.IntegerField(blank=True, null=True)
    answer_json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subquestion'
