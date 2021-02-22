from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from .models import Testimonials,LatestWorkWD,About,Contact,Blog,LatestWorkP,LatestWorkK

# Create your views here.
# def index(request):
#     clients = Testimonials.objects.all()
#     about =About.objects.all()
#     return render(request,'index.html',{'clients':clients}) 

# class HomeTemplateView(TemplateView):
#     template_name= 'index.html'
    
#     ##multiple value haru return render yeutai page ma garba mildaina so.
#     def get_context_data(self,**kwargs):
#         context =super().get_context_data(**kwargs) #suruma super lai call gareko context data laai
#         context['about']= About.objects.first()
#         context['clients']= Testimonials.objects.all()
#         context['workwds'] =LatestWorkWD.objects.all()
#         context['workps'] =LatestWorkP.objects.all()
#         context['workks'] =LatestWorkK.objects.all()
#         context['blogs'] =Blog.objects.all()
        
        

#         return context 
        
def index(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name ,email=email, desc=desc,date=datetime.today())
        contact.save()
    return render(request,'index.html')
        

