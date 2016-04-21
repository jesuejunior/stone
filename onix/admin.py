from onix.models import Question, Lesson, Answer, Unity, Media, Result

from django.contrib import admin


class UnityAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name', 'description', )
    list_filter = ('number', 'name', 'description', )
    search_fields = ('id', 'number', 'name', 'description', )

admin.site.register(Unity, UnityAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'extra')
    list_filter = ('name', 'extra',)

admin.site.register(Answer, AnswerAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name', )


admin.site.register(Lesson, LessonAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', )
    list_filter = ('name', )

admin.site.register(Media, MediaAdmin)


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'answer_correct', 'lesson', 'audio', 'image')
    list_filter = ('name', 'lesson')
    ordering = ['id']
    search_fields = ('id', 'name', 'answer_correct', 'lesson', )
    filter_horizontal = ('answers', )

    def lookup_allowed(self, lookup, value):
        return True


admin.site.register(Question, QuestionAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lesson', 'correct', 'question',)
    list_filter = ('user', 'lesson', 'correct', 'question',)

admin.site.register(Result, ResultAdmin)
