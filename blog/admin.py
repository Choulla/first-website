from django.contrib import admin
from .models import Blog
# Register your models here.

# class AdminInclude(admin.ModelAdmin): 
# 	list_display = ["__str__","pub_date"]
# 	class Meta:
# 		model = Blog
admin.site.register(Blog)
