from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, PageNotAnInteger
from qa.models import Question, Answer
import datetime

def test (request, *args, **kwargs):
	now = datetime.datetime.now()
	html =  "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def paginate(qs, request):
	paginator = Paginator(qs,10)
	paginator.baseurl = '/?page='
	page = request.GET.get('page')
	try:
		page = paginator.page(page)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page

@require_GET
def question_all (request):
	questions = Question.objects.order_by('-added_at')
	paginator = Paginator(questions,10)
	paginator.baseurl= '/?page='
	page = request.GET.get('page')
	try:
		page=paginator.page(page)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		page = paginator.page(paginator.num_pages) 
	
	return render (request,'questions_all.html',{
		'questions':page.object_list,
		'paginator':paginator, 'page':page,
		})

@require_GET	
def popular(request):
	questions = Question.objects.order_by('-rating')
	page=paginate(questions,request)
	
	return render (request,'popular.html',{
		'questions':page.object_list,
		'page':page,
		})

def question(request,question_id):
	try:
		qu=Question.objects.get(pk=question_id)
	except Question.DoesNoExist:
		raise Http404("Question no found")
	answers=Answer.objects.filter(question__pk=question_id)
	return render (request,"question.html",{
		'question':qu,
		'answers':answers
		})


# Create your views here.
