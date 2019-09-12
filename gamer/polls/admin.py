from django.contrib import admin
from polls.models import Questions , Choice

# Register your models here.

admin.site.site_header="Gamer polls"
admin.site.site_title ="Gamer admin"
admin.site.index_title="Welcome to Gamer poll admin"
class Choiceinline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets =[(None, {'fields':['question_text']}),('Date information', 
    {'fields':['pub_date'],'classes':['collapse']}),]
    inlines= [Choiceinline]

admin.site.register(Questions,QuestionsAdmin)

# admin.site.register(Choice)