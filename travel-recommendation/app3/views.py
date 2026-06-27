from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Datas, Place
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout    
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Datas, Place, BusRoute



def home(request):
    return render(request, 'index1.html')

def search_bus(request):
    source = request.GET.get('source', '').strip()
    destination = request.GET.get('destination', '').strip()
    date = request.GET.get('date', '').strip()

    results = []

    if source and destination and date:
        routes = BusRoute.objects.filter(
            starting__icontains=source,
            destination__icontains=destination,
        )
        for route in routes:
            results.append({
                'route': route,
                'available_seats': route.available_seats(date),
                'date': date,
            })

    return render(request, 'search_result.html', {
        'results': results,
        'source': source,
        'destination': destination,
        'date': date,
    })


@login_required
def booking(request):
    mydata = Datas.objects.filter(user=request.user)
    return render(request, 'booking_ticket.html', {'datas': mydata})

@login_required
def mybooking(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        arraival = request.POST.get('arraival')
        date = request.POST.get('date')
        time = request.POST.get('time')
        seat = request.POST.get('seat')
        name = request.POST.get('name')

        if not all([departure, arraival, date, time, seat, name]):
            messages.error(request, "All fields are required.")
            return redirect('booking')

        Datas.objects.create(
            user=request.user,
            starting=departure,
            destination=arraival,
            date=date,
            time=time,
            seat=seat,
            name=name,
        )
        messages.success(request, "Booking successful!")
        return redirect('booking')
    
    return render(request, 'booking_ticket.html')

@login_required
def updateData(request, id):
    mydata = get_object_or_404(Datas, id=id, user=request.user)

    if request.method == 'POST':
        mydata.starting = request.POST.get('departure', mydata.starting)
        mydata.destination = request.POST.get('arraival', mydata.destination)
        mydata.date = request.POST.get('date', mydata.date)
        mydata.time = request.POST.get('time', mydata.time)
        mydata.seat = request.POST.get('seat', mydata.seat)
        mydata.name = request.POST.get('name', mydata.name)
        mydata.save()
        messages.success(request, "Booking updated successfully!")
        return redirect('booking')
    
    return render(request, 'update.html', {'data': mydata})

@login_required
def deleteData(request, id):
    if request.method == 'POST':
        mydata = get_object_or_404(Datas, id=id, user=request.user)
        mydata.delete()
        messages.success(request, "Booking deleted successfully!")
        return redirect('booking')
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
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('passw')
        rpass = request.POST.get('pass')

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect('signup')
            
        if password != rpass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        if len(password) < 8:   
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')
        
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Sign-up successful!")
        return redirect('login')
    
    return render(request, 'signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index1')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
                auth_login(request, user)  # Log the user in
                messages.success(request, "Login successful!")
                next_url = request.GET.get('next', 'index1')  # Redirect to 'next' if available, else to 'index1'
                return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")


    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)  # Clears the session and logs out the user
    messages.success(request, "You have been logged out.")
    return redirect('index1')  
