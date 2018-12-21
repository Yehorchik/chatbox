from django.shortcuts import render,redirect
from .models import User , Message
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'newapp/index.html')

def signup(request):
    return render(request,'newapp/signup.html')

def login(request):
    return render(request,'newapp/login.html')

def welcome(request):
    messages.error(request,'Successfully registered')
    return render(request,'newapp/welcome.html')
def chat(request):
    if not 'userid' in request.session:
        messages.error(request,'Please log in')
        return redirect('/login')
    else:
        context ={
              'me' : User.objects.get(id=request.session['userid']),
              'all' : User.objects.all(),
              'mymessage' : Message.objects.all(),
              'messagecount': Message.objects.filter(sent_to=request.session['userid']).count(),

        }
        return render(request,'newapp/chat.html',context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            print(key)
            print(value)
            messages.error(request, value, extra_tags = key)
            # redirect the user back to the form to fix the errors
        return redirect('/signup')
    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash1)
    request.session['userid']=User.objects.last().id
    request.session['fname']=User.objects.last().first_name
    return redirect('/welcome')

def comein(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            # redirect the user back to the form to fix the errors
        return redirect('/login')		
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['userid']=user.id
        request.session['fname']=user.first_name
        return redirect('/main')

def info(request,id):
    x=User.objects.get(id=id)
    context={
        'user' : x
    }
    return render(request,'newapp/info.html',context)
def addfriend(request,id):
    friend=User.objects.get(id=id)
    context={
        'me' : friend,
    }
    me=User.objects.get(id=request.session['userid'])
    me.friends.add(friend)
    return render(request,'newapp/new.html',context)
def removefriend(request,id):
    me=User.objects.get(id=request.session['userid'])
    friend=User.objects.get(id=id)
    context={
       'i' : friend,
    }
    me.friends.remove(friend)
    return render(request,'newapp/remove.html',context)

def send_message(request,id):
    who=User.objects.get(id=request.session['userid'])
    to=User.objects.get(id=id)
    Message.objects.create(message=request.POST['message'],sent_from=who,sent_to=to)
    messages.error(request,'Your message succesffuly sent')
    return redirect('/main')
     
def delete_message(request,id):
    x=Message.objects.get(id=id)
    x.delete()
    return redirect('/main')
   
def logout(request):
    request.session.clear()
    return redirect('/login')


def back(request):
    return redirect('/main')


def update(request):
    x=User.objects.get(id=request.session['userid'])
    if request.POST['first_name']:
        x.first_name=request.POST['first_name']
    if request.POST['last_name']:
        x.last_name=request.POST['last_name']
    if request.POST['email']:
        x.email=request.POST['email']
    if request.POST['birthday']:
        x.birthday=request.POST['birthday']
    if request.POST['status']:
        x.status=request.POST['status']
    x.save()
    messages.error(request,'Your info succesffuly update')
    return redirect('/main')