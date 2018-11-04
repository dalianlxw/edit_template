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

class chapter(models.Model):
	id = models.AutoField(primary_key=True)
	subjectId = models.ForeignKey(subject,on_delete=models.CASCADE)
	pharseId = models.ForeignKey(pharse,on_delete=models.CASCADE)
	gradeId = models.ForeignKey(grade,on_delete=models.CASCADE)
	editionId = models.ForeignKey(edition,on_delete=models.CASCADE)
	chapter = models.CharField(max_length=255)
	unit = models.CharField(max_length=255)
	section = models.CharField(max_length=255)
	knowledgeId = models.IntegerField()
	chapterOrder = models.IntegerField()
	unitOrder = models.IntegerField()
	sectionOrder = models.IntegerField()

	def __init__(self):
		return self.id

class knowledge_level(models.Model):
	knowlevelId = models.AutoField(primary_key=True)
	subjectId = models.ForeignKey(subject,on_delete=models.CASCADE)
	pharseId = models.ForeignKey(pharse,on_delete=models.CASCADE)
	knowledge_level_1 = models.ForeignKey(knowledge_basic,to_field=knowledge_base.id,on_delete=models.CASCADE)
	knowledge_level_2 = models.ForeignKey(knowledge_basic,to_field=knowledge_base.id,on_delete=models.CASCADE)
	knowledge_level_3 = models.ForeignKey(knowledge_basic,to_field=knowledge_base.id,on_delete=models.CASCADE)
	knowledgeId = models.ForeignKey(knowledge_basic,to_field=knowledge_base.id,on_delete=models.CASCADE)
	level1 = models.CharField(max_length=255)
	level2 = models.CharField(max_length=255)
	level3 = models.CharField(max_length=255)

	def __init__(self):
		return self.knowlevelId

class questions(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.TextField(verbose_name="试题-题干")
	option_a = models.TextField(verbose_name="选项A")
	option_b = models.TextField(verbose_name="选项B")
	option_c = models.TextField(verbose_name="选项C")
	option_d = models.TextField(verbose_name="选项D")
	option_e = models.TextField(verbose_name="选项E")
	answer1 = models.TextField(verbose_name="标准答案")
	answer2 = models.TextField(verbose_name="非标准格式答案或含部分过程说明的答案")
	pharse = models.TextField(verbose_name="试题解析")
	qtpye = models.CharField(max_length=80,verbose_name="试题题型")
	diff = models.floatField()
	md5 = models.CharField(max_length=50,verbose_name="试题题干的md5值")
	subjectId = models.ForeignKey(subject,on_delete=models.CASCADE)
	gradeId = models.ForeignKey(grade,on_delete=models.CASCADE)
	knowledges = models.ForeignKey(knowledge_basic_id,on_delete=models.CASCADE)
	Area = models.CharField(max_length=50)
	year = models.IntegerField()
	paperTpye = models.CharField(max_length=50)
	source = models.CharField(max_length=200)
	fromSite = models.CharField(max_length=50)
	isSub = models.IntegerField(max_length=1)
	isNormal = models.IntegerField(max_length=1)
	isKonw = models.IntegerField(max_length=1)
	tiid = models.CharField(max_length=50)
	Similarity = models.IntegerField(max_length=5,default=0)
	isunique = models.IntegerField(max_length=2)
	md52 = models.CharField(max_length=50)

	def __init__(self):
		return self.id

class question_knowledge_basic_id(models.Model):
	id = models.AutoField(primary_key=True)
	knowledge_basic_id = models.ForeignKey(knowledge_basic,on_delete=models.CASCADE)
	question_id = models.ForeignKey(questions,on_delete=models.CASCADE)

	def __init__():
		return self.id

class subquestion(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.TextField()
	option_a = models.TextField()
	option_b = models.TextField()
	option_c = models.TextField()
	option_d = models.TextField()
	option_e = models.TextField()
	pid = models.IntegerField()
	answer1 = models.TextField(verbose_name="标准答案")
	answer2 = models.TextField(verbose_name="非标准格式答案或含部分过程说明的答案")
	pharse = models.TextField(verbose_name="试题解析")
	qtpye = models.CharField(max_length=80,verbose_name="试题题型")
	diff = models.floatField()
	md5 = models.CharField(max_length=50,verbose_name="试题题干的md5值")
	subjectId = models.ForeignKey(subject,on_delete=models.CASCADE)
	gradeId = models.ForeignKey(grade,on_delete=models.CASCADE)
	knowledges = models.ForeignKey(knowledge_basic_id,on_delete=models.CASCADE)
	source = models.CharField(max_length=200)
	tiid = models.CharField(max_length=50)
	ptiid = models.CharField(max_length=50)
 	fromSite = models.CharField(max_length=50)
 	answer_json = models.TextField()
