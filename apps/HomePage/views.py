from django.shortcuts import render


def homepage(request):
    data = {

    }
    return render(request, 'HomePage/index.html', data)
