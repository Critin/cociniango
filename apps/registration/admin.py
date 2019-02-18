from django.contrib import admin

from .models import Profile, Premio

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age')

admin.site.register(Premio)
