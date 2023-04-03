from django.shortcuts import render
from .models import User, Loan, Equipment

app_name = 'webPortal'

def index(request):
    context={}
    return render(request, 'webPortal/index.html', context) 

def userloans(request):
    #userid will be taken from session, putting in placeholder user for now
    userid = 1
    user = User.object.get(user=userid)
    username = user.
    userloans = Loan.objects.get(user=userid)

    num_userloans = userloans.count()

    
    context={
        'userloans': userloans,
        'num_userloans': num_userloans,
    }
    return render(request, 'webPortal/userloans.html', context)
