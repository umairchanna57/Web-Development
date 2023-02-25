from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import Save
# Create your views here.
@login_required(login_url='Login')

def Home(request): 
    return render(request, "Home.html")

def Signup(request):

    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Login')
        

    return render (request,'Signup.html')

def Login(request):
  
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Login.html')

def Logout(request):
    logout(request)
    return redirect('Login')


def Doctor(request):
       return render(request, 'Doctor.html')



def Appoinment(request):
     return render(request, 'Appoinment.html')

    

def About(request):
    return render(request, 'About.html')


def Save(request):
     n=''
     if request.method=="POST":

        nam = request.POST['name']
        Phon = request.POST['phone']
        Emai =request.POST['email']
        Dat = request.POST['date']
        Tim =request.POST['time']
        Are=request.POST['area']
        Cit=request.POST['city']
        Stat=request.POST['state']
        Postal_cod=request.POST['post-code']
        en=Save(name=nam, Phone=Phon, Email=Emai, Date=Dat, Time=Tim , Area=Are , City=Cit , State=Stat , Postal_code=Postal_cod)
        en.save() 
        n='Data Inserted'    
        return render(request, 'Appointment.html', {'n':n} )