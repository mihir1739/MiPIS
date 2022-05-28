from django.shortcuts import render,redirect
import random, string
from MiPIS.models import Data
from MiPIS.compare import compare
from django.http import HttpResponse,HttpResponseRedirect 
from MiPIS.forms import SignUpForm,LoginForm,DataForm,EditForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from MiPIS.notify import sendsms

global scores
global CURR_USER 

app_name = 'MiPIS'

def index(request): 
    '''
    returns Home Page view.
    '''
    return render(request,'index.html') 


def about(request):
    '''
    returns the About Page.
    '''
    return render(request,'about.html')


def register(request):
    '''
    A view to register new users.
    '''
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('username')
            scores[usr]= 0
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    '''
    view for existing users to login
    '''
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_user:
                CURR_USER = request.user.username
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form})


def admin(request):
    return render(request,'admin.html')

def employee(request):
    return render(request,'employee.html')


def customer(request):
    dat = Data.objects.all()
    st = {
        "data":dat
    }
    return render(request,'user.html',st)

@login_required
def database(request):
    msg = None
    if request.method == 'POST':
        form = DataForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            picture = form.cleaned_data.get('picture')
            age = form.cleaned_data.get('age')
            form.save()
            msg = "Form saved"
            return redirect('employee')
        else:
            msg = 'form is not valid'
    else:
        form = DataForm()
    return render(request, 'data.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

#view for submitting the data as a user
@login_required
def update(request,id):
    dis = Data.objects.get(id=id)
    if(request.method == 'POST'):
        form = EditForm(request.POST,request.FILES)
        if form.is_valid():
            similiar = form.cleaned_data.get('similiar')
            loc = form.cleaned_data.get('location')
            data = Data(id=id,similiar=similiar,age=dis.age,name=dis.name,picture=dis.picture,location=loc)
            data.save()
            dis = Data.objects.get(id=id)
            acc = compare(str(dis.picture), str(dis.similiar))
            data = Data(id=id,similiar=similiar,age=dis.age,name=dis.name,picture=dis.picture,location=loc,accuracy=acc)
            data.save()
            return HttpResponse(f"the accuracy was{acc}")
        else:
            msg = 'form is not valid'
    else:
        form = EditForm()
    return render(request, 'submit.html', {'form': form})

@login_required
def approve(request):
    dat = Data.objects.all()
    st = {
        "data":dat
    }
    return render(request,'approve.html',st)

@login_required   
def foundem(request,id):
    if(request.method == 'GET'):
        dis = Data.objects.get(id=id)
        if sendsms(dis.contact,dis.location,dis.name):
            dis.delete()
            return HttpResponse("Notified Complaint Lodger!")
        else:
            return HttpResponse("Couldn't Notify the Authorities!")
        return redirect('approve')
    else:
        return redirect('approve')
    
@login_required
def fake_call(request,id):
    if(request.method == 'GET'):
        dis = Data.objects.get(id = id)
        data = Data(id=id,age=dis.age,name=dis.name,picture=dis.picture,contact=dis.contact)
        data.save()
        return redirect('approve')
    else:
        return redirect('approve')

def daer():
    score_sorted_keys = sorted(scores, key=scores.get, reverse=True)
    tbr = {}
    for i in score_sorted_keys:
        tbr[i] = scores[i]
    return tbr

@login_required
def leaderboard(request):
    return render(request,'scores.html',{'tbr':tbr})

