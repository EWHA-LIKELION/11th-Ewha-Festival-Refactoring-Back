import imp
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'nickname', 'password', 'is_booth','is_show', 'is_tf', 'created_at', 'updated_at']
	list_display_links = ['id', 'username', 'nickname']