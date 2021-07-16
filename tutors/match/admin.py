from django.contrib import admin
from .models import *

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("id", "first_name", "last_name", "student_id", "gender", "age", "grade1", "grade2", "grade3", "parental_status", "guardian", "intention", "romantic", "extra_curr", "alcohol_cons", "result") #Set display in admin to list these columns
    search_fields = ("first_name", "last_name" ) #Create a search box to search these fields 
    list_filter = ("age", "gender", "parental_status", "guardian", "intention", "romantic", "extra_curr", "alcohol_cons")

class PassAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("id", "student", "learning_styles", "personality_styles", "area_of_interests") #Set display in admin to list these columns
    search_fields = ("student", ) #Create a search box to search these fields 
    list_filter = ("learning_styles", "personality_styles", "area_of_interests")

class FailAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("id", "student", "learning_styles", "personality_styles", "area_of_interests") #Set display in admin to list these columns
    search_fields = ("student", ) #Create a search box to search these fields 
    list_filter = ("learning_styles", "personality_styles", "area_of_interests")

class MatchAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("id", "student", "tutor") #Set display in admin to list these columns
    search_fields = ("student", ) #Create a search box to search these fields 

admin.site.register(Students, StudentsAdmin)  
admin.site.register(Pass, PassAdmin) 
admin.site.register(Fail, FailAdmin) 
admin.site.register(Match, MatchAdmin)