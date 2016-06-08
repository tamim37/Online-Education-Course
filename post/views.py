
from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render
from .models import *



num=5


# Create your views here.
def post_home(request):
	return render(request ,"index2.html",{})
def post_create(request):
	return HttpResponse("hello create page")
def post_detail(request):
	query=Post_model.objects.all()
	context={	
	"my_object_list":query
	
}
	return render(request,"index.html",context)

def login_check(request):
	username=request.GET['firstname']
	userpass=request.GET['password']
	

	login_name_in_query = Student.objects.filter(name=username,password=userpass)

	if login_name_in_query.exists():
		global studentName
		studentName=username


		print "yes it has that user name "
		abc={
			"name": username
		}

		return render(request,"dashboard.html",abc)

	else:
		print "no this user name is not in the list"	 #if some_queryset.exists():
		return HttpResponse("wrong username or password")

	
def homePageView(request):
	stdName=request.GET['std']

	all_course_list = Course_list_model.objects.all()
	a=CrsTaken.objects.all()


	abc={
		"name": stdName,
		"hmm":a,
		"context_course_list":all_course_list,
	}

	return render(request,"dashboard.html",abc)
	

def course_list_show(request):

	stdName=request.GET['std']

	print stdName

	all_course_list = Course_list_model.objects.all()
	context2={

		"context_course_list":all_course_list,
		"name":stdName,
	}

	return render(request,"course_list.html",context2)

def course_detail_view_fnc(request):
	# course_metarials = Course_list_model.objects.all()
	
	stdName=request.GET['std']

	
	x=request.GET['hidden_course_name']
	
	course_metarials = Course_list_model.objects.get(course_name=x)
	teachers=course_metarials.instructors.all()

	p=course_metarials.course_no
	

	usertable2=Student.objects.get(name=stdName)

	q=usertable2.crsToTake.filter(crs_no=p)

	if q:
		context={
			"context3_course_metarials":course_metarials,
			"instructorsName":teachers,
			"name":stdName,

		}
		
		return render(request,"single_course_metarial_show2.html",context)


	

	# user registration kora  na thakle

	

	context={
		"context3_course_metarials":course_metarials,
		"instructorsName":teachers,
		"name":stdName,

	}
	

	# return HttpResponse("hello details page")
	return render(request,"single_course_metarial_show.html",context)

	 # user reistration kora  thakle



def demoShow(request):
	z=request.GET['takenCourseNo']
	stdName=request.GET['std']
	cName=request.GET['crsName']

	v=CourseMetarial.objects.get(crs_no=z)

	usertable=Student.objects.get(name=stdName)
	usertable.crsToTake.add(v)

	try:

		getStd=CrsTaken.objects.get(crsNo=z)
		# weekQues=VideoSection.objects.get(weekNnumber__weekNo=weekno,
		# 	weekNnumber__course__crs_no=crsno)
		# videoinfo=weekQues.video
		amount=getStd.stdAmount

	except CrsTaken.DoesNotExist:
		getStd=CrsTaken(crsNo=z,stdAmount=0,crsname=cName)
		getStd.save()
		amount=getStd.stdAmount





	# getStd=CrsTaken.objects.get(crsNo=z)

	# amount=getStd.stdAmount
	print "type print----------------------"
	y=(int)(amount)
	print type(amount)
	print y
	print type(y)
	x=y+1

	print x

	CrsTaken.objects.filter(crsNo=z).update(stdAmount=x)



	return HttpResponse("free registraton success")
	


def regCrsShowView(request):
	z=request.GET['takenCourseNo']
	stdName=request.GET['std']	

	course_metarials = CourseMetarial.objects.get(crs_no=z)
	xx=course_metarials.courseWeek
	crsNo=course_metarials.crs_no
	context3={
		"context3_course_metarials":course_metarials,
		"yy":xx,
		"crs_No":crsNo,
		"name":stdName,

	}
	
	return render(request,"_7registered_crs_show.html",context3)
	
	

def weekElementView(request):
	z=request.GET['takenCourse']
	y=request.GET['weekNo']
	weeekAmount=request.GET['weekAmount']
	stdName=request.GET['std']


	course_metarials=Week.objects.filter(course__crs_no=z,course__courseWeek=y )
	
	context4={
		"context4_course_metarials":course_metarials,
		"a":y,
		"b":z,
		"weekAmount":weeekAmount,
		"name":stdName,

	}


	return render(request,"_8pageMetarialShow.html",context4)


def quizShowView(request):
	weekNo=request.GET['hiddenWeekNo']
	crsNo=request.GET['hiddenCrsNo']
	stdName=request.GET['std']


	weekQues=QuizSection.objects.filter(weekCount__weekNo=weekNo,
		weekCount__course__crs_no=crsNo)

	
	context5={
		"context5CourseMetarials":weekQues,
		"a":weekNo,
		"b":crsNo,
		"name":stdName,
		
	}

	return render(request,"_9quizPageShow.html",context5)


def quizQuestionView(request):
	mweekno=request.GET['hiddenWeekNo']
	ncrsno=request.GET['hiddenCrsNo']	
	p=request.GET['quizno']
	stdName=request.GET['std']
	
	abc=QuizSection.objects.get(weekCount__weekNo=mweekno,
		weekCount__course__crs_no=ncrsno,quizNo=p)

	abcd=abc.questionList.all();
	weekcnt=abcd.count()


	context={
		"quizno":abc,
		"questions":abcd,
		"a":mweekno,
		"b":ncrsno,
		"count":weekcnt,
		"name":stdName,
		
	}

	return render(request,"_10quesShow.html",context)





def videoShowView(request):
	weekno=request.GET['hiddenWeekNo']
	crsno=request.GET['hiddenCrsNo']
	weekAmounts=request.GET['Amount']
	stdName=request.GET['std']

	print weekno+" "+crsno

	try:


		weekQues=VideoSection.objects.get(weekNnumber__weekNo=weekno,
			weekNnumber__course__crs_no=crsno)
		videoinfo=weekQues.video
	except VideoSection.DoesNotExist:
		weekQues=None
	# quizSec.save()

	if weekQues:
		context={

			"videos":videoinfo,
			"weekNo":weekno,
			"crsNo":crsno,
			"weekAmount":weekAmounts,
			"name":stdName,
		
		
		}

		return render(request,"_11videoShow.html",context)

	context={

			# "videos":videoinfo,
			"weekNo":1,
			"crsNo":crsno,
			"weekAmount":weekAmounts,
			"name":stdName,
		
		
		}
	return render(request,"_11videoShow.html",context)

		












def teacherLogInPage(request):
	return render(request,"teacherLoginPageShow.html")


def teacherInfoCheck(request):
	tecName=request.GET['teacherName']
	userpass=request.GET['passWord']
	

	login_name_in_query = Teacher_model.objects.filter(teacher_name=tecName,teacher_pass=userpass)

	if login_name_in_query.exists():
		
		
		abc={
			"tecName": tecName
		}

		return render(request,"_1teacherDashboard.html",abc)

	else:
		print "no this user name is not in the list"	 #if some_queryset.exists():
		return HttpResponse("wrong username or password")


def tecHomePageView(request):
	tecName=request.GET['teacherName']
	abc={
			"tecName": tecName,
		}

	return render(request,"_1teacherDashboard.html",abc)




def techerCourseShow(request):
	# all_course_list = Course_list_model.objects.all()
	tecName=request.GET['teacherName']

	
	techersCoursesQueue=Course_list_model.objects.filter(instructors__teacher_name=tecName)

	context2={

		"teacherCourselist":techersCoursesQueue,
		"tecName": tecName,
	}

	return render(request,"_2teacherCourseListShow.html",context2)

	
def teacherCourseAdd(request):
	# all_course_list = Course_list_model.objects.all()
	
	return render(request,"_3tecAddCourse.html")

	
def techerCourseAdd2(request):
	# all_course_list = Course_list_model.objects.all()

	crsName=request.GET['Cname']
	crsNo=request.GET['Cno']
	csrSyl=request.GET['Csyllabus']
	crsTec=request.GET['Cteachers']
	# crsTec2=request.GET['Cteachers2']
	crsInfo=request.GET['Cinfo']

	crsInit=CrsTaken(crsNo=crsNo,stdAmount=0,crsname=crsName)
	crsInit.save()


	
	if request.method == 'GET' and 'Cteachers2' in request.GET:


		crsTec2 = request.GET['Cteachers2']
		if crsTec2:
			print crsTec2

	teacherAdd=Teacher_model.objects.filter(teacher_name=crsTec)
	# teacherAdd2=Teacher_model.objects.filter(teacher_name=crsTec2)

# teacher already in the list 
	if teacherAdd.exists():


		tec=Teacher_model.objects.get(teacher_name=crsTec)

		newCrs=Course_list_model(course_name=crsName,course_no=crsNo,course_syllabus=csrSyl,course_additional_info=crsInfo)
		newCrs.save()
		newCrs.instructors.add(tec)

		context={
			"qrsNo":crsNo,
			"crsName":crsName,
	
		}

		return render(request,"_4tecAddMetarialNow.html",context)

# New techer added

	teacherAdd=Teacher_model(teacher_name=crsTec)
	teacherAdd.save()

	newCrs=Course_list_model(course_name=crsName,course_no=crsNo,course_syllabus=csrSyl,course_additional_info=crsInfo)
	newCrs.save()
	newCrs.instructors.add(teacherAdd)

	context={
			"qrsNo":crsNo,
			"crsName":crsName,
	
	}
	
	return render(request,"_4tecAddMetarialNow.html",context)

def addWeekAmount(request):
	# all_course_list = Course_list_model.objects.all()

	crsName=request.GET['Cname']
	crsNo=request.GET['Cno']
	crsWeek=request.GET['Cweek']

	print crsNo
	print crsName
	print crsWeek
	print type(crsWeek)

	y=int(crsWeek)
	print type(y)
	
	crsToAdd=Course_list_model.objects.get(course_name=crsName,course_no=crsNo)

	print "--------------"

	newCrs=CourseMetarial(crs_no=crsNo,metarialNo=crsToAdd,courseWeek=crsWeek)
	newCrs.save()
	# newCrs.metarialNo.add(crsToAdd)

	


	elements = []

# then use the range function to do 0 to 5 counts
	for i in range(1,y+1):
		elements.append(i)
    	

# now we can print them out too
	# for i in elements:
 #    	print "Element was: %d" % i

	
	context={
			"qrsNo":crsNo,
			"crsWeek":y,
			"weekArray":elements,
	
	}

	return render(request,"_5tecselectWeek.html",context)


def insertInWeek(request):

	myWeekNo=request.GET['insertedWeekNo']
	mycrsNo=request.GET['x']
	
	print mycrsNo

	# foreign key add

	crsToAdd=CourseMetarial.objects.get(crs_no=mycrsNo)

	newCrs=Week(weekNo=myWeekNo,course=crsToAdd)
	newCrs.save()
	context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,
	
	}
	

	return render(request,"_6addQuizVideo.html",context)



def addQuizQuestion(request):

	myWeekNo=request.GET['WeekNo']
	mycrsNo=request.GET['crsNo']
	
	print mycrsNo
	print myWeekNo

	context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,
	
	}
	
	return render(request,"_7tecQuestionAddPage.html",context)
	# return render(request,"_7tecQuestionAddPage.html")


def addQuestionOrFinish(request):

	myWeekNo=request.GET['WeekNo']
	mycrsNo=request.GET['crsNo']
	ques=request.GET['question']
	op1=request.GET['op1']
	op2=request.GET['op2']
	op3=request.GET['op3']
	op4=request.GET['op4']
	ans=request.GET['ans']

	
	print mycrsNo
	print myWeekNo
	print op1 ,op2,op3,op4

	newQues=QuizQuestion(question=ques,option1=op1,option2=op2,
		option3=op3,option4=op4,answerField=ans)
	newQues.save()

# 	try:
#    to_friend = User.objects.get(username=friend_q)
# except User.DoesNotExist:
#    to_friend = None
	try:


		quizSec=QuizSection.objects.get(quizNo=1,weekCount__weekNo=myWeekNo,
			weekCount__course__crs_no=mycrsNo)
	except QuizSection.DoesNotExist:
		quizSec=None
	# quizSec.save()

	if quizSec:
		print "already exists  so add into many to many field only"
		quizSec.questionList.add(newQues)

	else:

		foreignValue=Week.objects.get(weekNo=myWeekNo,
			course__crs_no=mycrsNo)

		quesSec=QuizSection(quizNo=1,weekCount=foreignValue)
		quesSec.save()

		quesSec.questionList.add(newQues)


	


	if 'btn1' in request.GET:


		context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,
	
		}

		return render(request,"_7tecQuestionAddPage.html",context)

    # do some listing...
	elif 'btn2' in request.GET:


		return HttpResponse("finish adding into quiz section")
    # do something else

	
def Finish(request):

	

	if 'btn3' in request.GET:

		return HttpResponse("finish adding into quiz section")

	




def teacherEditCrs(request):
	tecName=request.GET['teacherName']
	print tecName+"----------------"

	techersCoursesQueue=Course_list_model.objects.filter(instructors__teacher_name=tecName)

	context={

		"teacherCourselist":techersCoursesQueue
	}

	return render(request,"_20tecEditCourse.html",context)




	
def editPageView(request):
	
	mycrsNo=request.GET['crsNo']
	mycrsName=request.GET['courseName']

	context={

		"crsNo":mycrsNo,
		"crsName":mycrsName,
	}

	return render(request,"_21tecEditQuizVideo.html",context)


	
def editQuizView(request):
	
	mycrsNo=request.GET['crsNo']
	mycrsName=request.GET['crsName']

	myCrsWeek=CourseMetarial.objects.get(crs_no=mycrsNo)
	print myCrsWeek.courseWeek

	y=int(myCrsWeek.courseWeek)

	elements = []

# then use the range function to do 0 to 5 counts
	for i in range(1,y+1):
		elements.append(i)
    	
	context={
			"crsNo":mycrsNo,
			"crsWeek":y,
			"weekArray":elements,
	
	}

	return render(request,"_22tecEditWeek.html",context)


def addNewQuizInTheWeek(request):

	myWeekNo=request.GET['insertedWeekNo']
	mycrsNo=request.GET['crsNo']
	print "-------------"
	print mycrsNo
	print myWeekNo

	context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,
			
	
	}

	return render(request,"_24tecOption.html",context)
	

def createnewQuiz(request):
	myWeekNo=request.GET['WeekNo']
	mycrsNo=request.GET['crsNo']
	myQuizNo=request.GET['quizNo']

	quizNoInAWeek=QuizSection.objects.filter(weekCount__weekNo=myWeekNo,
		weekCount__course__crs_no=mycrsNo)

	print type(quizNoInAWeek.count())
	
	y=quizNoInAWeek.count()+1


	# foreignValue=Week.objects.get(weekNo=myWeekNo,
	# 		course__crs_no=mycrsNo)
	# quizsec=QuizSection(quizNo=y,weekCount=foreignValue)
	# quizsec.save()
	if 'btn1' in request.GET:
		context={
				"crsNo":mycrsNo,
				"WeekNo":myWeekNo,
				"quizNo":y,
	
		}
	
		return render(request,"_23tecQuesEdit.html",context)
	if 'btn2' in request.GET:

		addedQuizNo=request.GET['qNo']

		context={
				"crsNo":mycrsNo,
				"WeekNo":myWeekNo,
				"quizNo":addedQuizNo,
	
		}
	
		return render(request,"_23tecQuesEdit.html",context)

	if 'btn3' in request.GET:

		removedQuizNo=request.GET['removedQNo']
		
		#  remove 

		try:


			quizSec=QuizSection.objects.get(quizNo=removedQuizNo,weekCount__weekNo=myWeekNo,
				weekCount__course__crs_no=mycrsNo)
		except QuizSection.DoesNotExist:
			quizSec=None
	# quizSec.save()

		if quizSec:
			print "already exists  so add into many to many field only"
			quizSec.delete()

			return HttpResponse("delete Successful")

		return HttpResponse("This week No not Found")




def editQuestionOrFinish(request):

	myWeekNo=request.GET['WeekNo']
	mycrsNo=request.GET['crsNo']
	myQuizNo=request.GET['quizNo']
	ques=request.GET['question']
	op1=request.GET['op1']
	op2=request.GET['op2']
	op3=request.GET['op3']
	op4=request.GET['op4']
	ans=request.GET['ans']

	

	newQues=QuizQuestion(question=ques,option1=op1,option2=op2,
		option3=op3,option4=op4,answerField=ans)
	newQues.save()


	try:


		quizSec=QuizSection.objects.get(quizNo=myQuizNo,weekCount__weekNo=myWeekNo,
			weekCount__course__crs_no=mycrsNo)
	except QuizSection.DoesNotExist:
		quizSec=None
	# quizSec.save()

	if quizSec:
		print "already exists  so add into many to many field only"
		quizSec.questionList.add(newQues)

	else:

		x=CourseMetarial.objects.get(crs_no=mycrsNo)
# ##
		foreignValue=Week(weekNo=myWeekNo,course=x)
		foreignValue.save()

		quesSec=QuizSection(quizNo=myQuizNo,weekCount=foreignValue)
		quesSec.save()

		quesSec.questionList.add(newQues)


	


	if 'btn1' in request.GET:


		context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,
			"quizNo":myQuizNo,
	
		}

		return render(request,"_23tecQuesEdit.html",context)

    # do some listing...
	elif 'btn2' in request.GET:


		return HttpResponse("finish adding into quiz section")
    # do something else










# 
def videoAddPage(request):
	
	mycrsNo=request.GET['crsNo']
	# mycrsName=request.GET['crsName']

	myCrsWeek=CourseMetarial.objects.get(crs_no=mycrsNo)
	print myCrsWeek.courseWeek

	y=int(myCrsWeek.courseWeek)

	elements = []

# then use the range function to do 0 to 5 counts
	for i in range(1,y+1):
		elements.append(i)
    	
	context={
			"crsNo":mycrsNo,
			"crsWeek":y,
			"weekArray":elements,
	
	}

	return render(request,"_71videoTecAdd.html",context)


def videoAddPage2(request):

	myWeekNo=request.GET['insertedWeekNo']
	mycrsNo=request.GET['crsNo']
	

	context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,	
	
	}

	return render(request,"_72.html",context)
	

def videoAddPage3(request):

	myWeekNo=request.GET['insertedWeekNo']
	mycrsNo=request.GET['crsNo']
	fileName=request.GET['videoFile']

	print fileName+"}}}}}}}}}}}}}}}}}}}}}}}}}}}}"+myWeekNo

	print type(fileName)


	try:


		addVideo=VideoSection.objects.get(weekNnumber__weekNo=myWeekNo,
			weekNnumber__course__crs_no=mycrsNo,video=fileName)
	except VideoSection.DoesNotExist:
		addVideo=None

	if addVideo:
		# already inserted so no need to insert again
		return HttpResponse("OKKKKKKKKKKK")


	else:
		# add and print OK
		try:

			getWeek=Week.objects.get(weekNo=myWeekNo,course__crs_no=mycrsNo)

		except Week.DoesNotExist:
			foreignCrs=CourseMetarial.objects.get(crs_no=mycrsNo)
			getWeek=Week(weekNo=myWeekNo,course=foreignCrs)
			getWeek.save()

		vidAdd=VideoSection(weekNnumber=getWeek,video=fileName)
		vidAdd.save()


		return HttpResponse("added successfully")


	
	

	context={
			"crsNo":mycrsNo,
			"WeekNo":myWeekNo,	
	
	}

	return render(request,"_72.html",context)





def crsDetailViewForTec(request):
	
	tecName=request.GET['teacherName']
	# crsName=request.GET['hidden_course_name']
	mycrsNo=request.GET['hiddenCrsNo']
	

	course_metarials = CourseMetarial.objects.get(crs_no=mycrsNo)
	weekAmount=course_metarials.courseWeek

	context={

		"crsNo":mycrsNo,
		"tecName":tecName,
		# "crsName":crsName,
		"weekAmount":weekAmount,
		"weekNo":1,
	}

	return render(request,"_61.html",context)

def crsDetailViewForTec2(request):

	weekno=request.GET['hiddenWeekNo']
	crsno=request.GET['hiddenCrsNo']
	weekAmounts=request.GET['Amount']
	tecName=request.GET['teacherName']


	try:


		weekQues=VideoSection.objects.get(weekNnumber__weekNo=weekno,
			weekNnumber__course__crs_no=crsno)
		videoinfo=weekQues.video
	except VideoSection.DoesNotExist:
		weekQues=None
	

	if weekQues:
		context={

			"videos":videoinfo,
			"weekNo":weekno,
			"crsNo":crsno,
			"weekAmount":weekAmounts,
			"tecName":tecName,
		
		
		}

		return render(request,"_62.html",context)

	context={

			# "videos":videoinfo,
			"weekNo":weekno,
			"crsNo":crsno,
			"weekAmount":weekAmounts,
			"tecName":tecName,
		
		}
	return render(request,"_62.html",context)

		












def quizForTec(request):
	crsNo=request.GET['hiddenCrsNo']
	tecName=request.GET['teacherName']
	weekNo=request.GET['hiddenWeekNo']	
	# tecname=request.GET['teacherName']
	# weekAmount=request.GET['Amount']
	print "xxxxxxxxxxxxxxxxxxxxxx"
	print "1111"+" "+weekNo+"     "+"22222222222"

	course_metarials = CourseMetarial.objects.get(crs_no=crsNo)
	weekAmount=course_metarials.courseWeek
	# crsNo=course_metarials.crs_no
	context3={
		"context3_course_metarials":course_metarials,
		"weekAmount":weekAmount,
		"crsNo":crsNo,
		"tecName":tecName,
		"weekNo":weekNo,

	}
	
	return render(request,"_63.html",context3)
	
	



def quizForTec2(request):
	weekNo=request.GET['hiddenWeekNo']
	crsNo=request.GET['hiddenCrsNo']
	tecName=request.GET['teacherName']
	weekAmount=request.GET['Amount']


	
	print "-------====================="+weekNo+" "+crsNo+" "+weekAmount

	try:


		weekQues=QuizSection.objects.filter(weekCount__weekNo=weekNo,
		weekCount__course__crs_no=crsNo)

		

	except QuizSection.DoesNotExist:
		weekQues=None
		

	if weekQues:
		context5={
			"context5CourseMetarials":weekQues,
			"weekNo":weekNo,
			"crsNo":crsNo,
			"tecName":tecName,
			"weekAmount":weekAmount,
		
		}

		return render(request,"_64.html",context5)




	context5={
		"context5CourseMetarials":weekQues,
		"weekNo":weekNo,
		"crsNo":crsNo,
		"tecName":tecName,
		"weekAmount":weekAmount,
		
	}

	return render(request,"_64.html",context5)


def quizForTec3(request):
	mweekNo=request.GET['hiddenWeekNo']
	ncrsNo=request.GET['hiddenCrsNo']	
	p=request.GET['quizno']
	tecName=request.GET['teacherName']
	weekAmount=request.GET['Amount']
	
	abc=QuizSection.objects.get(weekCount__weekNo=mweekNo,
		weekCount__course__crs_no=ncrsNo,quizNo=p)

	abcd=abc.questionList.all();
	weekcnt=abcd.count()


	context={
		"quizno":abc,
		"questions":abcd,
		"a":mweekNo,
		"weekNo":mweekNo,
		"b":ncrsNo,
		"crsNo":ncrsNo,
		# "weekAmount":weekAmount,
		"count":weekcnt,
		"tecName":tecName,
		"weekAmount":weekAmount,
		
	}

	return render(request,"_65.html",context)













def blogView(request):
	weekAmount=request.GET['weekAmount']
	# crsno2=request.GET['takenCourse']

	crsno=request.GET['hiddenCrsNo']
	
	stdName=request.GET['std']

	print " "+crsno+"-++++++++++++++++++"
	print " "+stdName+"-++++++++++++++++++"
	# print " "+crsno+"-++++++++++++++++++"

	
	


	try:



		blogs=Blog.objects.get(course__crs_no=crsno)
		blogComments=blogs.commentsList.all()

	except Blog.DoesNotExist:
		blogs=None
		blogComments=None

	if blogs:
		print "in if condition---------------------"

		context={

			"com":blogComments,
			"yy":weekAmount,
			"crsNo":crsno,
			"name":stdName,
		
		}

	else:
		print "in else condition---------------------"
		context={

			"com":blogComments,
			"yy":weekAmount,
			"crsNo":crsno,
			"name":stdName,
		
		}

	return render(request,"_51blog.html",context)




def addComView(request):

	weekAmount=request.GET['weekAmount']

	crsno=request.GET['hiddenCrsNo']	
	stdName=request.GET['std']
	comboxElement=request.GET['comBox']
	print comboxElement+"       "+crsno


	if comboxElement:
		print comboxElement
		
		commentAdd=Comments(comment=comboxElement,userName=stdName)
		commentAdd.save()

		crsToAdd2=CourseMetarial.objects.get(crs_no=crsno)

		try:

			blogs=Blog.objects.get(course__crs_no=crsno)
			blogs.commentsList.add(commentAdd)
			print "-----------"
			print "-----------"
			print "-----------"
			# blogComments=blogs.commentsList.all()



		
		except Blog.DoesNotExist:
			blogAdd=Blog(course=crsToAdd2)
			blogAdd.save()
			blogAdd.commentsList.add(commentAdd)
			# blogs=None
			# blogComments=None


	try:

		blogs=Blog.objects.get(course__crs_no=crsno)
		# blogs.commentsList.add(commentAdd)
		blogComments=blogs.commentsList.all()


	except Blog.DoesNotExist:
		blogs=None
		blogComments=None

	if blogs:
		print "in if condition---------------------"

		context={

			"com":blogComments,
			"yy":weekAmount,
			"crsNo":crsno,
			"name":stdName,
		
		}

	else:
		print "in else condition---------------------"
		context={

			"com":blogComments,
			"yy":weekAmount,
			"crsNo":crsno,
			"name":stdName,
		
		}

	return render(request,"_51blog.html",context)







def myCrsView(request):

	stdName=request.GET['std']

	print stdName

	stdlist = Student.objects.get(name=stdName)
	stdCrsList=stdlist.crsToTake.all()
	context2={

		"context_course_list":stdCrsList,
		"name":stdName,
	}

	return render(request,"_81.html",context2)

	# return HttpResponse("aaaaa");





def StdSignUpView(request):

	return render(request,"_91StdSignUp.html")

	# return HttpResponse("aaaaa");


def StdEntryAddView(request):

	stdName=request.GET['firstname']
	passwd=request.GET['password']
	passwd2=request.GET['password2']

	print passwd+" "+passwd2


	if (passwd==passwd2):
		stdlist = Student(name=stdName,password=passwd)
		stdlist.save()
		return HttpResponse("signup successful")

	else:
		return HttpResponse("password doesnot match")



def tecSignUpView(request):

	return render(request,"_92tecSignUp.html")


def tecEntryAddView(request):

	tecName=request.GET['firstname']
	passwd=request.GET['password']
	passwd2=request.GET['password2']

	print passwd+" "+passwd2


	if (passwd==passwd2):
		teclist = Teacher_model(teacher_name=tecName,teacher_pass=passwd)
		teclist.save()
		return HttpResponse("signup successful")

	else:
		return HttpResponse("password doesnot match")

