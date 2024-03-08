from django.contrib import admin

# Register your models here.
from .models import CategoryMovie,Movie,Profile

admin.site.register(CategoryMovie)
admin.site.register(Movie)
admin.site.register(Profile)