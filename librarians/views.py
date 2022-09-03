from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_librarian(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('catalog:index')
            
        else:
            messages.success(request, ("Please enter a valid username and password."))
            return redirect('librarians:login')
            # Return an 'invalid login' error message.
          
    else:
        return render(request, 'authenticate/login.html', {})

def logout_librarian(request):
    logout(request)
    messages.success(request, ("Logout Successful."))
    return redirect('catalog:index')



