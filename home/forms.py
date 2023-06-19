from django import forms
from .models import Player, PlayerManager, PlayerPosition
from attr import fields
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlayerForm(forms.Form):
    class Meta:
        model = Player
        fields = '__all__'
        
        
class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']