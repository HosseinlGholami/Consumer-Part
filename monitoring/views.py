from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def ODD_OR_EVEN(num):
    if(num%2==0):
        return "Even"
    else:
        return "ODD"

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












#____________________________________
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
