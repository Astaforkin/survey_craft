from asyncore import poll
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import AnswerOption, Poll, Question, UserAnswer
from django.contrib.auth.decorators import login_required

    


def home(request):
    
    return render(request, 'quiz/home.html')    

@login_required 
def polls(request):
    context = {
        'polls': Poll.objects.all()
    }
    return render(request, 'quiz/polls.html', context)

def detail(request, poll_id):
    try:
        id = Poll.objects.get( id = poll_id )
    except:
        raise Http404("Тест не найден!")

    return render(request, 'quiz/polls.html', {'poll': id})

def questions(request, poll_id):
    context = {
        'questions': Question.objects.filter( poll_id = poll_id).order_by('order', 'id'),
        'poll': Poll.objects.get(id = poll_id)
    }

    return render(request, 'quiz/questions.html', context)

def have_next_question():
    pass

def question_detail(request, question_id):
    try:
        user_answer = UserAnswer.objects.get(question_id = question_id, user=request.user)
    except:
        user_answer = None
    
    disabled = ''
    if user_answer:
        disabled = 'disabled'

    context = {
        'question' : Question.objects.get( id = question_id ),
        'answer_options' : AnswerOption.objects.filter( question_id = question_id ),
        'disabled' : disabled,
        'user_answer' : user_answer
    }
    if request.method == 'POST':
        answer_option_id = request.POST.get('answer_option')
        if answer_option_id:
            UserAnswer.objects.create(user=request.user, question_id=question_id, answer_options_id=answer_option_id)
            return redirect('question_detail', question_id)

    return render(request, 'quiz/question_detail.html', context)

def populate_poll():
    poll = Poll.objects.create(title='Математический тест')
    question1 = Question.objects.create(text='2 + 2 = ?', order = '1', poll=poll)
    question2 = Question.objects.create(text='2 / 2 = ?', order = '2', poll=poll)
    question3 = Question.objects.create(text='3 + 2 = ?', order = '3', poll=poll)
    question4 = Question.objects.create(text='2 - 1 = ?', order = '4', poll=poll)
    question1_answer1 = AnswerOption.objects.create(text='1', points = '0', question=question1)
    question1_answer2 = AnswerOption.objects.create(text='4', points = '1', question=question1)
    question2_answer1 = AnswerOption.objects.create(text='1', points = '1', question=question2)
    question2_answer2 = AnswerOption.objects.create(text='0', points = '0', question=question2)
    question3_answer1 = AnswerOption.objects.create(text='10',points = '0', question=question3)
    question3_answer2 = AnswerOption.objects.create(text='5', points = '1', question=question3)
    question4_answer1 = AnswerOption.objects.create(text='4', points = '0', question=question4)
    question4_answer2 = AnswerOption.objects.create(text='1', points = '1', question=question4)
