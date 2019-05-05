from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('questtion_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['questtion_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)