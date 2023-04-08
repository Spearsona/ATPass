from django.shortcuts import render
from .models import AtUser, LoanInstance
app_name = 'webPortal'

def index(request):
    context={}
    return render(request, 'webPortal/index.html', context) 

def userloans(request):
    #userid will be taken from session, putting in placeholder user for now
    atuserid = 1
    
    atuser = AtUser.objects.get(id=1)
    
    userloans = LoanInstance.objects.filter(atuser=atuserid)

    num_userloans = userloans.count()

    context={
        'atuser': atuser,
        'userloans': userloans,
        'num_userloans': num_userloans,
    }
    return render(request, 'webPortal/userloans.html', context)

