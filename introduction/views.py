from django.shortcuts import render


def introduction(request):
    return render(request, 'introduction.html')


def aboutMe(request):
    return render(request, 'aboutMe.html')