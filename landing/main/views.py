from django.shortcuts import render
from .models import *



def main_page(request):
	all_news = NewsModel.objects.all()
	all_teachers = TeachersModel.objects.all()
	all_programs = ProgramsModel.objects.all()
	return render(request, 'main/main_page.html', {'all_news':all_news, 
		'all_teachers':all_teachers, 'all_programs':all_programs})


def programs_page(request):
	all_programs = ProgramsModel.objects.all()
	return render(request, 'main/programs.html', {'all_programs':all_programs, })


def news_page(request):
	all_news = NewsModel.objects.all()
	return render(request, 'main/news.html', {'all_news':all_news, })


def about_page(request):
	abouts = AboutUniversityModel.objects.all()
	return render(request, 'main/about.html', {'abouts':abouts, })

