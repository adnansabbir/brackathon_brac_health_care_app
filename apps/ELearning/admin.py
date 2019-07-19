from django.contrib import admin
from apps.ELearning.models import Tutorial, McqQuestions, McqAnswers, UserTutorialMap, UserMcqQuestionMap

admin.site.register(Tutorial)
admin.site.register(McqQuestions)
admin.site.register(McqAnswers)
admin.site.register(UserTutorialMap)
admin.site.register(UserMcqQuestionMap)

# Register your models here.
