from django.shortcuts import render, get_object_or_404
from .models import Answer, Choice, Tag, Question


# Create your views here.
def home(request):
    questions = Question.objects.all_objects()
    return render(request, 'poll/home.html', {'questions': questions})


def question_details(request, question_id):
    questions = Question.objects.all_objects() # Include 'inactive' questions
    question = get_object_or_404(questions, id=question_id)
    return render(request, 'poll/question_details.html', {'question': question})
