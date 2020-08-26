from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView , DetailView
from django.views.generic.edit import FormView ,CreateView ,DeleteView
import random
from .models import CreateConsumer, CreateQueue
from .form   import ConsumerCreatFormClassic ,ConsumerCreatForm,QueueCreatForm

from .rabbitmq import rbmq
import time ,pika
thread_handeller=dict()

import requests

class monitoringView(TemplateView):
    template_name = "monitoring.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Queue_objs=CreateQueue.objects.all()
        auth=requests.auth.HTTPBasicAuth('hgh', 'guest')
        qs=list()
        for obj in  Queue_objs:
            url='http://127.0.0.1:15672/api/queues/%2F/'+obj.slug+'/'
            data=requests.get(url=url,auth=auth).json()
            qs.append(data)
        context={
            "Page_name":"monitoring Queue Page",
            "Queue_Detail_json":qs
        }
        return context


def QueuDelete(request,*args, **kwargs):
    print('Delete Queue  : '+ kwargs.get('slug') )
    obj=CreateQueue.objects.get( slug = kwargs.get('slug') )
    obj.delete()
    return HttpResponseRedirect("/queue")

def ConsumerDelete(request,*args, **kwargs):
    print('Delete Consumer  : '+ kwargs.get('slug') )
    obj=CreateConsumer.objects.get( slug = kwargs.get('slug') )
    obj.delete()
    return HttpResponseRedirect("/consumer")


# Create your views here.
class QueueDetailView(DetailView):
    template_name = "QueueDetail.html"
    queryset = CreateQueue.objects.all()
    
class QueueCreateView (CreateView):
    template_name="form.html"
    form_class=QueueCreatForm
    success_url="/queue"

class QueueView(TemplateView):
    template_name = "queue.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = CreateQueue.objects.all()
        context={
            "Page_name":"Queue Page",
            "object_list":queryset
        }
        return context

def Packet_Handeler_callback(ch, method, properties, body):
     print("Received   "+body.decode("utf-8") +" from :" +method.consumer_tag)
     time.sleep(1)
     ch.basic_ack(delivery_tag = method.delivery_tag)
     

def Consumingstart(request,*args, **kwargs):
    print('start consuming : ' +kwargs.get('slug') )
    obj=CreateConsumer.objects.get(slug=kwargs.get('slug') )
    
    if  CreateQueue.objects.filter(slug=obj.Queue_Name) :
        credentials = pika.PlainCredentials('hgh', 'guest')
        parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
        connection = rbmq(Slug=kwargs.get('slug'),Parameter=parameters,
                prefetch_count=obj.Pre_fetch,
                QueueName=obj.Queue_Name,
                CalbackFunc=Packet_Handeler_callback
                )
        thread_handeller.update({kwargs.get('slug'):connection})
        print(thread_handeller)
        connection.start()
    else:
        print("queue does not exist !")
    return HttpResponseRedirect("/consumer") 


def Consumingstop(request,*args, **kwargs):
    print('stop consuming : '+ kwargs.get('slug') )
    connction=thread_handeller.get(kwargs.get('slug'))
    if (connction!=None):
        connction.stop()
        thread_handeller.pop(kwargs.get('slug'))
    else:
        print("first you should to start it ")
    return HttpResponseRedirect("/consumer")


class ConsumerCreateView (CreateView):
    template_name="form.html"
    form_class=ConsumerCreatForm
    success_url="/consumer"

class ConsumerDetailView(DetailView):
    template_name = "consumerDetail.html"
    queryset = CreateConsumer.objects.all()


class ConsumerView(TemplateView):
    template_name = "consumer.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = CreateConsumer.objects.all()
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
