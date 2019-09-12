from django.shortcuts import render
from polls.models import Questions, Choice

# get questions and display them
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request, 'polls/index.html', context)

#specific questions and choices 
def details(request, question_id):
    try:
        questions = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question doesnot exist")
    return render  (request, 'polls/details.html', {'questions':questions})

#get questions and display results

def result(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render (request, 'polls/results.html', {'question':question})

