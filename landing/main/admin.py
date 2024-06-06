from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'date',)

class TeachersAdmin(admin.ModelAdmin):
	list_display = ('full_name',)

class ProgramsAdmin(admin.ModelAdmin):
	list_display = ('title',)

class AboutUniversityAdmin(admin.ModelAdmin):
	list_display = ('title',)

# class AboutUniversityModel(models.Model):
admin.site.register(NewsModel, NewsAdmin)
admin.site.register(TeachersModel, TeachersAdmin)
admin.site.register(ProgramsModel, ProgramsAdmin)
admin.site.register(AboutUniversityModel, AboutUniversityAdmin)