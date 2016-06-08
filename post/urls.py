
from django.conf.urls import patterns, include,url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', post_detail),
	url(r'home/$', post_home),
	url(r'^create/$', post_create),
	url(r'^login_check_list/$', login_check),
	url(r'course_list/$', course_list_show),
	url(r'single_course_detail/$', course_detail_view_fnc),
	url(r'courseAddToStudent/$', demoShow),
	url(r'regCrsShow/$', regCrsShowView),
	url(r'ToTheWeek/$',weekElementView),
	url(r'quizShow/$',quizShowView),
	url(r'quizNo/$',quizQuestionView),

	url(r'videoShow/$',videoShowView),


	
	url(r'homePage/$',homePageView),


	url(r'loginAsTeacher/$',teacherLogInPage),
	url(r'tecHomePage/$',tecHomePageView),
	url(r'checkTecherInfo/$',teacherInfoCheck),
	url(r'teacherCourse/$', techerCourseShow),
	url(r'addcourse/$',teacherCourseAdd),
	url(r'addCourse2/$', techerCourseAdd2),
	url(r'addWeek/$',addWeekAmount),
	url(r'insertIntoWeek/$', insertInWeek),
	url(r'addQuizes/$', addQuizQuestion),
	url(r'addSingleQuestion/$',addQuestionOrFinish),
	url(r'finishAdding/$',Finish),
	

	url(r'editCrs/$',teacherEditCrs),
	url(r'editPage/$',editPageView),
	url(r'editQuizes/$',editQuizView),
	url(r'editIntoWeek/$',addNewQuizInTheWeek),
	url(r'editQuestion/$',editQuestionOrFinish),
	url(r'createNew/$',createnewQuiz),

	url(r'addVideos/$',videoAddPage),
	url(r'addVideoIntoWeek2/$',videoAddPage2),
	url(r'addVideoIntoWeek3/$',videoAddPage3),






	
	url(r'courseDetailForTec/$',crsDetailViewForTec),
	url(r'videoShow2/$',crsDetailViewForTec2),
	url(r'quizShow2/$',quizForTec),
	url(r'tecQuiz/$',quizForTec2),
	url(r'tecQuiz3/$',quizForTec3),



	

	url(r'blogShow/$',blogView),
	url(r'addComment/$',addComView),

	
	url(r'myCrsShow/$',myCrsView),

	url(r'StdSignUp/$',StdSignUpView),
	url(r'StdEntryAdd/$',StdEntryAddView),

	
	url(r'signUpTec/$',tecSignUpView),
	url(r'tecEntryAdd/$',tecEntryAddView),


	

	# url(r'course_lis/$', course_list_show),



    
]

