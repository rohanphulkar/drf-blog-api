from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email','is_active','is_staff','is_admin')
    sortable_by = ('email')

admin.site.register(User, UserAdmin)
