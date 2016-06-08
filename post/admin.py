from django.contrib import admin

# Register your models here.
from django.contrib import admin
from post.models import *

class postmodelAdmin(admin.ModelAdmin):
	list_display=["title","content","updated"]
	list_filter=["updated","title"]
	class Meta:
		model=Post_model

admin.site.register(Post_model,postmodelAdmin)



class postmodelAdmin(admin.ModelAdmin):
	list_display=["name"]
	list_filter=["name"]
	class Meta:
		model=Student

admin.site.register(Student,postmodelAdmin)


class postmodelAdmin(admin.ModelAdmin):
	list_display=["teacher_name"]
	# list_filter=["course_name","course_no"]
	class Meta:
		model=Teacher_model

admin.site.register(Teacher_model,postmodelAdmin)


class postmodelAdmin(admin.ModelAdmin):
	list_display=["course_name","course_no"]
	list_filter=["course_name","course_no"]
	class Meta:
		model=Course_list_model

admin.site.register(Course_list_model,postmodelAdmin)




class postmodelAdmin(admin.ModelAdmin):
	list_display=["metarialNo"]
	#list_filter=["course_name2","course_no2"]
	class Meta:
		model=CourseMetarial

admin.site.register(CourseMetarial,postmodelAdmin)




class postmodelAdmin(admin.ModelAdmin):
	list_display=["date"]
	#list_filter=["course_name2","course_no2"]
	class Meta:
		model=RegistrationDate

admin.site.register(RegistrationDate,postmodelAdmin)



class postmodelAdmin(admin.ModelAdmin):
	list_display=["id"]
	#list_filter=["course_name2","course_no2"]
	class Meta:
		model=Week

admin.site.register(Week,postmodelAdmin)



class postmodelAdmin(admin.ModelAdmin):
	list_display=["id","crsNo","stdAmount"]

	class Meta:
		model=CrsTaken

admin.site.register(CrsTaken,postmodelAdmin)


class postmodelAdmin(admin.ModelAdmin):
	 list_display=["id"]
	 fieldsets = (
        (None, {
            'fields': ('question','option1','option2','option3','option4','answerField')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
             'fields': ('extraOption','extraAnswerField'),
        }),
    )



	 class Meta:
		model=QuizQuestion


admin.site.register(QuizQuestion,postmodelAdmin)

class postmodelAdmin(admin.ModelAdmin):
	 list_display=["quizNo","weekCount"]
	 



	 class Meta:
		model=QuizSection


admin.site.register(QuizSection,postmodelAdmin)




class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'option4','image')
        }),
        
    )
    class Meta:
		model=Demo
admin.site.register(Demo,FlatPageAdmin)		



class postmodelAdmin(admin.ModelAdmin):
	 list_display=["id","video"]
	 
	 class Meta:
		model=VideoSection


admin.site.register(VideoSection,postmodelAdmin)


class postmodelAdmin(admin.ModelAdmin):
	 list_display=["id"]
	 
	 class Meta:
		model=Blog


admin.site.register(Blog,postmodelAdmin)

class postmodelAdmin(admin.ModelAdmin):
	 list_display=["id"]
	 
	 class Meta:
		model=Comments


admin.site.register(Comments,postmodelAdmin)







