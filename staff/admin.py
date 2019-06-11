from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User
from .forms import CustomUserChangeForm ,CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (('User'), {'fields': ('username', 'first_name','last_name','email','is_staff', 'b_date')}),
        (('Permissions'), {'fields': ('is_active','is_staff')}),
    )

admin.site.register(User,CustomUserAdmin)
