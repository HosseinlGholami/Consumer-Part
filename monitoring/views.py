from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

#function based view 
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
    #response :
    num= random.randint(1,100)
    return render(request=request,template_name="base.html",context={"VARIABLE_A":"Hossein Gholami","NUM":num})
