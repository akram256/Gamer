from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.models import Questions, Choice

# get questions and display them
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request, 'polls/index.html', context)

#specific questions and choices 
def details(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question doesnot exist")
    return render  (request, 'polls/details.html', {'question':question })

#get questions and display results

def result(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render (request, 'polls/results.html', {'question':question})

#vote for a question
def vote(request, question_id):
    # print('jsdddnndndsnmdsnmdmndsmn',request.POST['choice'])
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
#         #redisplaying the voting form
        return render(request, 'polls/details.html', {'question':question,
        'error_message':"You didn't select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=( question.id,)))



