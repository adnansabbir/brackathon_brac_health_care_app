from django.shortcuts import render
from apps.ELearning.models import Tutorial


def tutorial_list(request):
    tutorials = Tutorial.objects.all().values('title')
    data = {
        'tutorials': tutorials
    }

    return render(request, 'ELearning/list.html', data)
