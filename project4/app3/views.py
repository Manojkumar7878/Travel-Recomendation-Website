from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.contrib.auth import logout

def home(request):
    return render(request, 'index1.html')


def booking(request):
    mydata = Datas.objects.all()
    return render(request, 'booking_ticket.html', {'datas': mydata})


def mybooking(request):
    if request.method == 'POST':
        departure = request.POST['departure']
        arraival = request.POST['arraival']
        date = request.POST['date']
        time = request.POST['time']
        seat = request.POST['seat']
        name = request.POST['name']

        obj = Datas(
            starting=departure,
            destination=arraival,
            date=date,
            time=time,
            seat=seat,
            name=name,
        )
        obj.save()
        return redirect('booking')
    return render(request, 'booking_ticket.html')


def updateData(request, id):
    mydata = get_object_or_404(Datas, id=id)
    if request.method == 'POST':
        mydata.starting = request.POST['departure']
        mydata.destination = request.POST['arraival']
        mydata.date = request.POST['date']
        mydata.time = request.POST['time']
        mydata.seat = request.POST['seat']
        mydata.name = request.POST['name']
        mydata.save()
        return redirect('booking')
    return render(request, 'update.html', {'data': mydata})

def deleteData(request, id):
    mydata = get_object_or_404(Datas, id=id)
    mydata.delete()
    return redirect('booking')

def place_list(request):
    places = Place.objects.all()
    return render(request, 'place_list.html', {'places': places})


def hire_bus(request):
    return render(request, 'hire_bus.html')

def help(request):

    return render(request, 'help.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('passw')
        rpass = request.POST.get('pass')

        if password != rpass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if Signup.objects.filter(user=user).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        obj = Signup(
            user=user,
            pasw=make_password(password),
            email=email,
        )
        obj.save()
        messages.success(request, "Sign-up successful!")
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_obj = Signup.objects.get(user=username)
            if check_password(password, user_obj.pasw):
                request.session['username'] = user_obj.user
                messages.success(request, "Login successful!")
                return redirect('index1')
            else:
                messages.error(request, "Invalid password.")
        except Signup.DoesNotExist:
            messages.error(request, "User does not exist.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)  # Clears the session and logs out the user
    messages.success(request, "You have been logged out.")
    return redirect('index1')  
