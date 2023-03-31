from django.shortcuts import render

app_name = 'webPortal'

def index(request):
    context={}
    return render(request, 'webPortal/index.html', context) 