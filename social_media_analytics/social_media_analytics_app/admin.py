from django.contrib import admin

from . models import Answer, Question


# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']



# Note: the two lines below register the Answer and Question classes
# so that Question & Answers are visible together in the admin site
# making Question & Answer input and deletion very fast

admin.site.register(Answer)
admin.site.register(Question)
