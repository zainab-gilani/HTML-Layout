# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
#
# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
#         min_length=8
#         )
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "password"]
#     #endclass
# #endclass
#
# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
# #endclass