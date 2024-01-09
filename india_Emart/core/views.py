from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from item.models import Category, Item 

from .forms import SignupForm

# Create your views here.
def index(request): 
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

"""
@login_required
def logout(request):
    logout(request)
    messages.info(request, "Logged out succesfully")
    return redirect('/login/')
"""
@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out succesfully")
    #return redirect('/login/')
    return render(request, 'core/logout.html')