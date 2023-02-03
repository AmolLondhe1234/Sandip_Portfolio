from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def cert(request):

    return render(request,'certificate.html')

def fb(request):

    return render(request,'feedback.html')
def home(request):

    return render(request,'home.html')

def prjt(request):
    return render(request,'project.html')