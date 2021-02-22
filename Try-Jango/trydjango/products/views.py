from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html',{})

def about(request,*args,**kwargs):
    my_context={
        "my_text":"this is about me",
        "my_number":123,
        "my_list":[134,56,89],

    }
    return render(request,'about.html',my_context)

def contact(request,*args,**kwargs):
    return render(request,'contact.html',{})