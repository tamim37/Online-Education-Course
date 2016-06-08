from __future__ import unicode_literals
from datetime import datetime
from django.db import models
#from django.db import models
from django import forms
from django.utils.html import format_html

# Create your models here. 

class Post_model(models.Model):
	title=models.CharField(max_length=30)
	content=models.TextField()
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)


	def __unicode__(self):
		return self.title


class Teacher_model(models.Model):
	teacher_name=models.CharField(max_length=30)
	teacher_pass=models.CharField(max_length=30,blank=True,null=True)
	

	def __unicode__(self):
		return self.teacher_name



class Course_list_model(models.Model):
	course_name=models.CharField(max_length=30)
	course_no=models.CharField(max_length=30)
	course_syllabus=models.CharField(max_length=500,  null=True)
	#course_syllabus=models.CharField(max_length=500, blank=True, null=True)

	instructors=models.ManyToManyField(Teacher_model)
	course_additional_info=models.CharField(max_length=30)


	def __unicode__(self):
		return "%s %s" % (self.course_name,self.course_no)

 # return "%s %s" % (self.first_name, self.last_name)
class CourseMetarial(models.Model):
	crs_no=models.CharField(max_length=20,null=True)
	metarialNo=models.ForeignKey(Course_list_model)
	courseWeek=models.IntegerField(null=True)


	def __unicode__(self):
		return self.crs_no

# class Quiz(models.Model):


class CrsTaken(models.Model):
	crsNo=models.CharField(max_length=20,null=True)
	stdAmount=models.CharField(max_length=5)
	crsname=models.CharField(max_length=20,null=True)
	

	def __unicode__(self):
		return self.crsNo



class Week(models.Model):
	weekNo=models.CharField(max_length=30,null =True)
	course=models.ForeignKey(CourseMetarial)

	def __unicode__(self):
		return "week:%s courseNo:%s" % (self.weekNo,str(self.course))


class QuizQuestion(models.Model):

	question=models.CharField(max_length=300,null=True)
	#options=models.ManyToManyField(Choice, related_name="options")
	option1=models.CharField(max_length=50,null=True)
	option2=models.CharField(max_length=50,null=True)
	option3=models.CharField(max_length=50,null=True)
	option4=models.CharField(max_length=50,null=True)

	answerField=models.CharField(max_length=100,null=True,blank=True)

	extraOption=models.CharField(max_length=50,null=True,blank=True)
	extraAnswerField=models.CharField(max_length=50,null=True, blank=True)
	

	def __unicode__(self):
		return u"%s" % self.id

class QuizSection(models.Model):

	quizNo=models.CharField(max_length=50)
	weekCount=models.ForeignKey(Week,null=True)
	questionList=models.ManyToManyField(QuizQuestion,blank=True)

	def __unicode__(self):
		return self.quizNo


class VideoSection(models.Model):

	# qzNo=models.CharField(max_length=50)
	weekNnumber=models.ForeignKey(Week,null=True)
	video=models.FileField(null=True,blank=True)
	# questionList=models.ManyToManyField(QuizQuestion,blank=True)

	def __unicode__(self):
		return u"%s" % self.id
		


class Demo(models.Model):
    name = models.CharField(max_length=400)
    option4=models.CharField(max_length=50)
    image=models.FileField(null=True,blank=True)

    def __unicode__(self):
		return self.name



class Student(models.Model):
	name=models.CharField("person's first name",max_length=30)
	password=models.CharField(max_length=30)

	crsToTake=models.ManyToManyField(CourseMetarial, blank=True)


	def __unicode__(self):
		return self.name


class Comments(models.Model):

	comment=models.CharField(max_length=300)
	# comment=models.CharField("person's first name",max_length=300)
	userName=models.CharField(max_length=90,null=True)
	time=models.DateTimeField(auto_now=False,auto_now_add=True,null=True,blank=True)
	# time2=models.DateTimeField(auto_now=True,auto_now_add=False,null=True,blank=True)

	# userName2=models.CharField(max_length=90,null=True)


	def  __unicode__(self):
		return u"%s" % self.id

class Blog(models.Model):

	commentsList=models.ManyToManyField(Comments, blank=True)
	course=models.ForeignKey(CourseMetarial)


	def  __unicode__(self):
		return u"%s" % self.id



class RegistrationDate(models.Model):

	date = models.DateField()
	std_id=models.ForeignKey(Student)
	crs_id=models.ForeignKey(CourseMetarial)

	def  __unicode__(self):
		return "%s" %(self.date)


