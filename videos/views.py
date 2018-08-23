from django.views import generic
from django.views.generic import DetailView
#from django.db.models import Queue
from .models import Movie
from bs4 import BeautifulSoup
import requests
import json
#list of our movies
class IndexView(generic.ListView):
	template_name = 'videos/index.html'
	model = Movie
	context_object_name = 'movie_data'#all movies in the database are stored in all_movies, to be used in index.html
	
	def search(request):
		template = 'videos/detail.html'
		query = request.GET.get("q")
		results = Movie.objects.filter(Q(title__icontains = query))[:5] # | = or

		# https://www.youtube.com/watch?v=-4_esavnIqo for info 5 minutes
		pages = pagination(request, results, num=1)

		context = {
			'item':pages[0]
		}
		return render(request, template, context)



	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(IndexView, self).get_context_data(**kwargs)
		#headings = ['Here are all my Movies:', 'Here are all my Movies made in 2010:']
		#context['headings'] = headings

		# Add in a QuerySet of all the books
		#context['all_movies'] = Movie.objects.all()

		context['movies_in_2010'] = Movie.objects.filter(year = 2010)[:5]

		return context

	def get_queryset(self):
		print("INSIDE")
		return Movie.objects.all()



class DetailView(generic.DetailView):
	model = Movie
	template_name = 'videos/detail.html'