from django.contrib import admin
from .models import AnswerOption, Poll, Question
admin.site.register(Poll)
admin.site.register(Question)


@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')