from django.contrib import admin
from .models import Artist, User

class ArtistInline(admin.StackedInline):
    model = Artist

class UserAdmin(admin.ModelAdmin):
    inlines = [ArtistInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
