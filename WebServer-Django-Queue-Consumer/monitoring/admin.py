from django.contrib import admin

# Register your models here.
from .models import CreateConsumer, CreateQueue

admin.site.register(CreateQueue)
admin.site.register(CreateConsumer)