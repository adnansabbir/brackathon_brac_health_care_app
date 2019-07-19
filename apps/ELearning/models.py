from django.db import models
from django.contrib.auth.models import User


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    readers = models.ManyToManyField(User, related_name='tutorial', through='UserTutorialMap')

    def __str__(self):
        return self.title


class McqQuestions(models.Model):
    user = models.ManyToManyField(User, related_name='answered_questions', through='UserMcqQuestionMap')
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='mcq_questions')
    question = models.CharField(max_length=255)
    marks = models.IntegerField()

    def __str__(self):
        return self.question


class McqAnswers(models.Model):
    question = models.ForeignKey(McqQuestions, on_delete=models.CASCADE, related_name='answers')
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option


class UserTutorialMap(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seen = models.BooleanField(default=True)


class UserMcqQuestionMap(models.Model):
    question = models.ForeignKey(McqQuestions, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(McqAnswers, on_delete=models.CASCADE)  # If true it was a correct answer

    def get_score(self):
        return self.answer.is_correct
