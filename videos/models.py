# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from bs4 import BeautifulSoup
import requests
import json

# Create your models here.


class Movie(models.Model):

	fn =  models.CharField(max_length = 100, default = 0)
	tid=  models.CharField(max_length = 50, default = 0) #tt123434
	title= models.CharField(max_length = 200, default = 0)
	wordsInTitle= models.CharField(max_length = 100, default = 0)
	url= models.CharField(max_length = 100, default = 0)
	imdbRating= models.FloatField(default = 0.0)
	ratingCount= models.IntegerField(default = 0)
	year= models.IntegerField(default = 0)
	type= models.CharField(max_length = 75, default = 0)
	nrOfWins= models.IntegerField(default = 0)
	nrOfNominations= models.IntegerField(default = 0)
	nrOfPhotos= models.IntegerField(default = 0)
	nrOfNewsArticles= models.IntegerField(default = 0)
	nrOfUserReviews= models.IntegerField(default = 0)

	def __str__(self):
		 return self.title
  
  	def getGenre(self):
  			response = requests.get(self.url)
			html = BeautifulSoup(response.content,'html.parser')
			tags = html.findAll("span",{"itemprop":"genre"})
			genres = []
			for genre in tags:
				genres.append(genre.text.strip())
			return genres


	def getPosterURL(self):
		try:
			response = requests.get(self.url)
			html = BeautifulSoup(response.content,'html.parser')
			posterURL = html.find(attrs={'class':'poster'}).find('img')['src']
			return posterURL  
		except:
			return "/static/videos/images/star2.png"
	
class Trailer(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)#will get deleted if the Movie linking to the trialer is deleted
	trailer_title = models.CharField(max_length = 250)
	#file_type = models.CharFieldi(max_length = 10)
	
	def __str__(self):
		return self.trailer_title + " for the movie " + self.movie.title