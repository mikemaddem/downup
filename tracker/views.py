from django.shortcuts import render


def index(request):
    return render(request, 'tracker/index.html')

def notfound(request, exception):
    return render(request, 'tracker/404.html')