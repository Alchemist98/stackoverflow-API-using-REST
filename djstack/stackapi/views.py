from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import QuestionSerializer
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
def index(request):
	return HttpResponse("Success")

class QuestionAPI(viewsets.ModelViewSet):
	#queryset is something from data will come
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

def latest(request):
	try:
		res = requests.get("https://stackoverflow.com/questions")
		soup = BeautifulSoup(res.text,"html.parser")
		questions = soup.select(".question-summary")

		for que in questions:
			q = que.select_one('.question-hyperlink').getText()
			vote_count = que.select_one('.vote-count-post').getText()
			views = que.select_one('.views').attrs['title']

			question = Question()
			question.question = q
			question.vote_count = vote_count
			question.views = views

			question.save()
		return HttpResponse("Latest Data Fetched from stackoverflow")

	except e as Exception:
		return HttpResponse(f"Failed {e}")