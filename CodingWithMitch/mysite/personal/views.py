from django.shortcuts import render
# from personal.models import Question
from account.models import Account
# Create your views here.
def  home_screen_view(request):
    context={}
    #     'name' :'Sujan',
    #     'address' :'Bharatpur-11,Chitwan',
    #     'list':[56,76,54,78],
    # }
    # questions =Question.objects.all()
    # context['questions']=questions
    users =Account.objects.all()
    context['accounts']=users

    return render(request,"personal/home.html",context)
