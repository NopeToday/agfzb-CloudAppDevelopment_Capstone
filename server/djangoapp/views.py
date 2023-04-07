from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def static_template_view(request):
    return render(request, 'static_template.html')
# Create an `about` view to render a static about page
# def about(request):
# ...
def about_view(request):
    return render(request, 'about.html')

# Create a `contact` view to return a static contact page
#def contact(request):
def contact_view(request):
    return render(request, 'contact.html')
# Create a `login_request` view to handle sign in request
# def login_request(request):
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to success page or homepage
            return redirect('djangoapp:index')  # Replace 'djangoapp:index' with the URL name of your homepage view
        else:
            # Handle invalid login credentials
            error_message = 'Invalid username or password.'
            return render(request, 'djangoapp/index.html', {'error_message': error_message})
    else:
        return render(request, 'djangoapp/index.html')

# Create a `logout_request` view to handle sign out request
# def logout_request(request):

def logout_view(request):
    logout(request)
    # Redirect to homepage or a success page
    return redirect('djangoapp:index') 

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
def registration_request(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        
        # Create new User object and save to database
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        # Redirect to login page
        return redirect('djangoapp:login')
    
    return render(request, 'djangoapp/registration.html')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

