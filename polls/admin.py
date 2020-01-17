from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date infomation', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
