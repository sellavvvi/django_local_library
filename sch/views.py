from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render 
from .models import Messages

def index(request):
     return render(request, 'sch/index.html')

def about_us(request):
     return render(request, 'sch/about_us.html')

def classes(request):
     return render(request, 'sch/classes.html')

def teachers(request):
     return render(request, 'sch/teachers.html')

def faq(request):
     return render(request, 'sch/faq.html')

def contact_us(request):
     if request.method == "POST":
          name_get = request.POST.get('name')
          email_get = request.POST.get('email')
          message_get = request.POST.get('message')
          if name_get and email_get and message_get:
               new_people = Messages(name=name_get, email=email_get, message=message_get)
               new_people.save()
     return render(request, 'sch/contact_us.html')

def page_not_found(request, exception):
     return render(request, "sch/page_404.html", status=404)
