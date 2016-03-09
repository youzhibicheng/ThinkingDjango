from django.contrib import admin

# Register your models here.

from models import Question
from models import Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

'''
class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']
'''

'''
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
'''

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['question_text']}),
		('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	# Customize the admin change list
	list_display = ('question_text', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['question_text']

#admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)