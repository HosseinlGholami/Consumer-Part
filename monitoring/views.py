from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView , DetailView
from django.views.generic.edit import FormView ,CreateView ,DeleteView
import random
from .models import Consumer
from .form   import ConsumerCreatFormClassic ,ConsumerCreatForm

from .rabbitmq import rbmq
import time ,pika
# Create your views here.
def Packet_Handeler_callback(ch, method, properties, body):
     print("Received"+body.decode("utf-8") +" from :" +method.consumer_tag)
     time.sleep(1)
     ch.basic_ack(delivery_tag = method.delivery_tag)

def Consumingstart(request,*args, **kwargs):
    print('start consuming : ' +kwargs.get('slug') )
    credentials = pika.PlainCredentials('hgh', 'guest')
    parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
    connection = rbmq(Slug=kwargs.get('slug'),Parameter=parameters,
              prefetch_count=2,
              QueueName='classic_queue_2',
              CalbackFunc=Packet_Handeler_callback
              )
    obj=Consumer.objects.get(slug=kwargs.get('slug'))
    obj.connection=connection
    obj.save()
    print(connection)
    connection.start()
    return HttpResponseRedirect("/consumer") 


def Consumingstop(request,*args, **kwargs):
    print('stop consuming : '+ kwargs.get('slug') )
    parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
    connection = rbmq(Slug=kwargs.get('slug'),Parameter=parameters,
              prefetch_count=2,
              QueueName='classic_queue_2',
              CalbackFunc=Packet_Handeler_callback
              )
    obj=Consumer.objects.get(slug=kwargs.get('slug'))
    print(connection == obj.connection)

    return HttpResponseRedirect("/consumer")


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
