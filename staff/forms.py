from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from .widgets import XDSoftDateTimePickerInput


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name','last_name','email','is_staff', 'b_date']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class DateForm(forms.Form):
    date = forms.DateTimeField(
                input_formats=['%d/%m/%Y %H:%M'],
                # widget=XDSoftDateTimePickerInput()
                )
