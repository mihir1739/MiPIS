from django.shortcuts import render,redirect
import random, string
from MiPIS.models import Data
from MiPIS.compare import compare
from django.http import HttpResponse,HttpResponseRedirect 
from MiPIS.forms import SignUpForm,LoginForm,DataForm,EditForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import PIL


app_name = 'MiPIS'

def index(request): 
    return render(request,'index.html') 

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
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


def customer(request):
    dat = Data.objects.all()
    st = {
        "data":dat
    }
    return render(request,'user.html',st)

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
def employee(request):
    return render(request,'employee.html')

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
            prev1 = dis.similiar
            prev2 = dis.location
            data = Data(id=id,similiar=similiar,age=dis.age,name=dis.name,picture=dis.picture,location=loc)
            data.save()
            dis = Data.objects.get(id=id)
            acc = compare(dis.picture, dis.similiar)
            datave = Data(id=id,similiar=similiar,age=dis.age,name=dis.name,picture=dis.picture,location=loc,accuracy=acc)
            data.save()
            return redirect('customer')
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
    
def foundem(request,id):
    if(request.method == 'GET'):
        dis = Data.objects.get(id=id)
        data = Data(id=id,similiar=dis.similiar,age=dis.age,name=dis.name,picture=dis.picture,location=dis.location,found=True)
        data.delete()
        return redirect('approve')
    else:
        return redirect('approve')