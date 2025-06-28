from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'authentication/login.html')

@csrf_protect
def simulate_csrf_error(request):
    if request.method == 'POST':
        return HttpResponse("Form submitted successfully!")
    return HttpResponse("GET request, please submit the form.")

def signup(request):
    return render(request, 'app/sign-up.html')

def index(request):
    return render(request, 'app/login.html')



# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from .forms import SignUpForm, CustomAuthenticationForm
# from django.contrib.auth.models import User
#
# def signup_view(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data["password"])
#             user.save()
#             login(request, user)
#             return redirect("logged-in-course-finder")
#         #endif
#     else:
#         form = SignUpForm()
#         return render(request, "app/sign-up/sign-up.html", {'form': form})
#     #endif
# #enddef
#
# def login_view(request):
#     if request.method == "POST":
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("logged-in-course-finder")
#         else:
#             form = CustomAuthenticationForm()
#         #endif
#         return render(request, "app/login/login.html")
#     #endif
# #enddef
#
# def logout_view(request):
#     logout(request)
#     return redirect("login")
# #enddef