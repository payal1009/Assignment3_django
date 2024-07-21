from .forms import FormClass
from django.shortcuts import render
from django.http import HttpResponse
from .models import modelClass
import re
from django.views.decorators.cache import cache_page
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.views import View
 
@receiver(post_save,sender=modelClass)
def call_mail_api(sender,instance,created,**kwargs):
    if created:
        send_mail(
            'Hello!',
            f'Hello {instance.name}, thank you for Joining Rubiscape Please submit ur Letter of Understanding!',
            'payalchougule109@gmail.com',
            [instance.email],
            fail_silently=False,
        )

class baseview(View):
    def get(self,request,*args,**kwargs):
        form=FormClass()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=FormClass(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            return HttpResponse("Thank you")
        
def home(request):
    return render(request, 'home.html')

# def cached(request):
#     x=get_user_model()
def showdata(request):
    if request.method=='POST':
        form=FormClass(request.POST)
        if form.is_valid():
            Ui=form.cleaned_data['i']
            Uname=form.cleaned_data['name']
            Upassword=form.cleaned_data['password']
            Uemail=form.cleaned_data['email']
            Udate=form.cleaned_data['date']
            status=form.cleaned_data['status']
            events = modelClass.objects.filter(i=Ui)
            if events.exists():
                return HttpResponse("id exist. please enter new id")
            uppercase_count = len(re.findall(r'[A-Z]', Upassword))
            lowercase_count = len(re.findall(r'[a-z]', Upassword))
            special_count = len(re.findall(r'[^A-Za-z0-9]', Upassword))
            numeric_count = len(re.findall(r'[0-9]', Upassword))
            if uppercase_count<=0 or lowercase_count<=0 or special_count<=0 or numeric_count<=0 or len(Upassword)<10:
                return HttpResponse("password length must be at least 10 and must contain at least one uppercase, one lowercase,one special character,one numeric value")
            user=modelClass.objects.create(i=Ui,name=Uname,password=Upassword,email=Uemail,date=Udate,status=status)
            user.save()
            return HttpResponse("data Saved")
    form=FormClass()
    return render(request,'register.html',{'form':form})


@cache_page(30)
def status(request):
    if request.method == 'POST':
        stat = request.POST.get('quantity')
        user_status = modelClass.objects.filter(status=stat)        
        return render(request, 'status.html', {'user_status': user_status})
    return render(request, 'status_enter.html')
    