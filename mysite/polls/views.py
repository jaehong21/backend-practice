from django import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Question

def index(request):
    lastest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list,}
    # output = ', '.join([q.question_text for q in lastest_question_list])
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/index.html', context)

def detail(request, question_id): 
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question},)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)