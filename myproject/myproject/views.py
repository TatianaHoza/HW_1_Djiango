from django.http import HttpResponse
from django.shortcuts import render
def aboutsite(request):
    return HttpResponse('<h1>This site about me</h1>')

def aboutme(request):
    return render(request,'about_me.html')
