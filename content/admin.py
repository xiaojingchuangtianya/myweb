from django.contrib import admin
from  .models import Blog
# Register your models here.
@admin.register(Blog)
class display(admin.ModelAdmin):
    list_display = ("title","classification","create_time","author")
