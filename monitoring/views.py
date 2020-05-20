from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , DetailView
from django.views.generic.edit import FormView ,CreateView ,DeleteView
import random
from .models import Consumer
from .form   import ConsumerCreatFormClassic ,ConsumerCreatForm

# Create your views here.

class ConsumerCreateView (CreateView):
    template_name="form.html"
    form_class=ConsumerCreatForm
    success_url="/consumer"

class ConsumerDetailView(DetailView):
    template_name = "consumerDetail.html"
    queryset = Consumer.objects.all()


class ConsumerView(TemplateView):
    template_name = "consumer.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Consumer.objects.all()
        context={
            "Page_name":"consumer Page",
            "object_list":queryset
        }
        return context

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num= random.randint(1,100)
        context={
            "Page_name":"Home Page:",
            "NAME":"Hossein Gholami",
            "NUM":num,
            "ODD_OR_EVEN":ODD_OR_EVEN(num),
            "SHOW_LUCKY": num%2 
        }
        return context
    
class ContactView(TemplateView):
    template_name = "contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={
        "Page_name":"Contact Page:",
        "NAME":"Hossein Gholami"
        }
        return context
    
class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={
        "Page_name":"About Page :"
        }
        return context
    














#____________________________________
def ODD_OR_EVEN(num):
    if(num%2==0):
        return "Even"
    else:
        return "ODD"

def oldhome(request):
    html__="""
<!DOCTYPE html>
<html lang="en">
    <header></header>
    <body>
        <h1>HelloWorld!</h1>
        <p>This is my first html code (hello from python Strings)  code</p>
    </body>
</html>
"""
    #response :
    return HttpResponse(html__)

def home(request):
    num= random.randint(1,100)
    contex={
        "Page_name":"Home Page:",
        "NAME":"Hossein Gholami",
        "NUM":num,
        "ODD_OR_EVEN":ODD_OR_EVEN(num),
        "SHOW_LUCKY": num%2 
    }
    return render(request=request,template_name="home.html",context=contex)

def about(request):
    contex={
        "Page_name":"About Page :"
    }
    return render(request=request,template_name="about.html",context=contex)

def contact(request):
    contex={
        "Page_name":"Contact Page:",
        "NAME":"Hossein Gholami"
    }
    return render(request=request,template_name="contact.html",context=contex)
