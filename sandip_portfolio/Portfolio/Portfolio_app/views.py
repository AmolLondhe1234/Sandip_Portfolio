from django.shortcuts import render,HttpResponse
from .models import Projects,Certificate,Feedback
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'home.html')

def cert(request):
    cert=Certificate.objects.all()
    context={
        'cert':cert
    }
    return render(request,'certificate.html',context)

def fb(request):
    if request.method == 'POST':
        fname = request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        mess= request.POST['feedback_text']
        Feedback(name=fname,email=email,phone=phone,feedback_text=mess).save()
        messages.success(request,'FeedBack Submited Successfully')
        return render(request,'feedback.html')
    elif request.method=='GET':
        return render(request,'feedback.html')
    else:
        # return HttpResponse("An error Occured! Employee Has Not Been added")
    
        return render(request,'feedback.html') 
    # return render(request,'feedback.html')
def home(request):

    return render(request,'home.html')

def prjt(request):
    prjt=Projects.objects.all()
    return render(request,'project.html',{'prjt':prjt})