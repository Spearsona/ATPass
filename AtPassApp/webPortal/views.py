from django.shortcuts import render
from .models import User, Loan, Equipment

app_name = 'webPortal'

def index(request):
    context={}
    return render(request, 'webPortal/index.html', context) 

def userloans(request):
    #userid will be taken from session, putting in placeholder user for now
    userid = 1
    user = User.objects.get(id=1)
    
    userloans = Loan.objects.filter(user=userid)
    equipment = []
    provider = []
    for loan in userloans:
        equipment.append(loan.equipment)
        provider.append(loan.provider)

    num_userloans = userloans.count()

    
    context={
        'user': user,
        'userloans': userloans,
        'num_userloans': num_userloans,
        'equipment': equipment,
        'provider':provider,
    }
    return render(request, 'webPortal/userloans.html', context)

