from __future__ import unicode_literals

from django.db import models

# Create your models here.
class edition(models.Model):
	Id = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=255)

	def __str__(self):
		return self.Id


class subject(models.Model):
	subjectId = models.IntegerField(primary_key=True)
	subjectName = models.CharField(max_length=255)
	pinyin = models.CharField(max_length=255)

	def __init__(self):
		return self.subjectId


class grade(models.Model):
	gradeId = models.IntegerField(primary_key=True)
	gradeName = models.CharField(max_length=255)

	def __init__(self):
		return self.gradeId


class pharse(models.Model):
	pharseId = models.IntegerField(primary_key=True)
	pharseName = models.CharField(max_length=255)

	def __init__(self):
		return self.pharseId

#class pharsegrade(object):
#	pharseId = models.IntegerField(primary_key=True)
#	gradeId = models.CharField(max_length=255)
#
#	def __init__(self):
#		return self.pharseId

class knowledge_basic(models.Model):
	id = models.AutoField(primary_key=True)
	knowledgeName = models.CharField(max_length=200,verbose_name="知识点名称")
	subjectId = models.ForeignKey(subject,on_delete=models.CASCADE,verbose_name="学科ID")
	pharseId = models.ForeignKey(pharse,on_delete=models.CASCADE,verbose_name="学历Id")
	key = models.CharField(max_length=500)
	descs = models.TextField()

	def __init__(self):
		return self.id
