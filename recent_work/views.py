from django.shortcuts import render


def recent_work(request):
    return render(request,'recent_work.html')