from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Question, Choice, User, Responses
from django.views.decorators.http import require_http_methods
import uuid

def home_redirect(request):
    return redirect('polls:questions')

def questions(request):
    question_list = Question.objects.all()[:5]  #Get the first 5 questions only
    context = {'questions': question_list}
    return render(request, 'polls/questions.html', context)

@require_http_methods(["POST"])
def submit(request):
    # Generate a unique user identifier
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))

        # Process each question and selected choice
    for question in Question.objects.all()[:5]:
       choice_id = request.POST.get(f'question_{question.id}')
       if choice_id:
                choice = get_object_or_404(Choice, pk=choice_id)
                response = Responses(user=user, question=question, choice=choice)
                response.save()
        
    return redirect('polls:thank_you')


def thank_you(request):
    questions = Question.objects.all()[:5]
    responses_summary = []

    for question in questions:
        choices = question.choice_set.all()
        response_count = {}
        
        max_count = 0
        most_selected_choice_text = ''

        for choice in choices:
            count = Responses.objects.filter(question=question, choice=choice).count()
            response_count[choice.choice_text] = count
            
            if count > max_count:
                max_count = count
                most_selected_choice_text = choice.choice_text
        
        responses_summary.append({
            'question': question,
            'response_count': response_count,
            'most_selected_choice_text': most_selected_choice_text
        })

    return render(request, 'polls/thank_you.html', {'responses_summary': responses_summary})

#Code for second template questions2.html

def questions2(request):
    question_list = Question.objects.all()[5:10] #from 5 to 10
    context = {'questions': question_list}
    return render(request,'polls/questions2.html', context)

def submit2(request):
    # Generate a unique user identifier
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))

    # Process each question and selected choice
    for question in Question.objects.all()[5:10]:  # Handle responses for the next 5 questions
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            response = Responses(user=user, question=question, choice=choice)
            response.save()

    return redirect('polls:thank_you2')

def thank_you2(request):
    questions = Question.objects.all()[5:10]
    responses_summary = []

    for question in questions:
        choices = question.choice_set.all()
        response_count = {}
        
        max_count = 0
        most_selected_choice_text = ''

        for choice in choices:
            count = Responses.objects.filter(question=question, choice=choice).count()
            response_count[choice.choice_text] = count
            
            if count > max_count:
                max_count = count
                most_selected_choice_text = choice.choice_text
        
        responses_summary.append({
            'question': question,
            'response_count': response_count,
            'most_selected_choice_text': most_selected_choice_text
        })

    return render(request, 'polls/thank_you2.html', {'responses_summary': responses_summary})

#Code for third template questions2.html

def questions3(request):
    question_list = Question.objects.all()[10:15] #from 5 to 10
    context = {'questions': question_list}
    return render(request,'polls/questions3.html', context)

def submit3(request):
    # Generate a unique user identifier
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))

    # Process each question and selected choice
    for question in Question.objects.all()[10:15]:  # Handle responses for the next 5 questions
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            response = Responses(user=user, question=question, choice=choice)
            response.save()

    return redirect('polls:thank_you3')

def thank_you3(request):
    questions = Question.objects.all()[10:15]
    responses_summary = []

    for question in questions:
        choices = question.choice_set.all()
        response_count = {}
        
        max_count = 0
        most_selected_choice_text = ''

        for choice in choices:
            count = Responses.objects.filter(question=question, choice=choice).count()
            response_count[choice.choice_text] = count
            
            if count > max_count:
                max_count = count
                most_selected_choice_text = choice.choice_text
        
        responses_summary.append({
            'question': question,
            'response_count': response_count,
            'most_selected_choice_text': most_selected_choice_text
        })

    return render(request, 'polls/thank_you3.html', {'responses_summary': responses_summary})

#Code for fourth template questions4.html

def questions4(request):
    question_list = Question.objects.all()[15:20] #from 5 to 10
    context = {'questions': question_list}
    return render(request,'polls/questions4.html', context)

def submit4(request):
    # Generate a unique user identifier
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))

    # Process each question and selected choice
    for question in Question.objects.all()[15:20]:  # Handle responses for the next 5 questions
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            response = Responses(user=user, question=question, choice=choice)
            response.save()

    return redirect('polls:thank_you4')

def thank_you4(request):
    questions = Question.objects.all()[15:20]
    responses_summary = []

    for question in questions:
        choices = question.choice_set.all()
        response_count = {}
        
        max_count = 0
        most_selected_choice_text = ''

        for choice in choices:
            count = Responses.objects.filter(question=question, choice=choice).count()
            response_count[choice.choice_text] = count
            
            if count > max_count:
                max_count = count
                most_selected_choice_text = choice.choice_text
        
        responses_summary.append({
            'question': question,
            'response_count': response_count,
            'most_selected_choice_text': most_selected_choice_text
        })

    return render(request, 'polls/thank_you4.html', {'responses_summary': responses_summary})

#Code for fifth template questions5.html

def questions5(request):
    question_list = Question.objects.all()[20:25]
    context = {'questions': question_list}
    return render(request, 'polls/questions5.html', context)

@require_http_methods(["POST"])
def submit5(request):
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))

    for question in Question.objects.all()[20:25]:
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            response = Responses(user=user, question=question, choice=choice)
            response.save()

    return redirect('polls:thank_you5')

def thank_you5(request):
    questions = Question.objects.all()[20:25]
    responses_summary = []

    for question in questions:
        choices = question.choice_set.all()
        response_count = {}
        
        max_count = 0
        most_selected_choice_text = ''

        for choice in choices:
            count = Responses.objects.filter(question=question, choice=choice).count()
            response_count[choice.choice_text] = count
            
            if count > max_count:
                max_count = count
                most_selected_choice_text = choice.choice_text
        
        responses_summary.append({
            'question': question,
            'response_count': response_count,
            'most_selected_choice_text': most_selected_choice_text
        })

    return render(request, 'polls/thank_you5.html', {'responses_summary': responses_summary})

#Code for fifth template questions5.html

def questions6(request):
    question_list = Question.objects.all()[25:30]
    context = {'questions': question_list}
    return render(request, 'polls/questions6.html', context)

@require_http_methods(["POST"])
def submit6(request):
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))

    for question in Question.objects.all()[25:30]:
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            response = Responses(user=user, question=question, choice=choice)
            response.save()

    return redirect('polls:thank_you6')

def thank_you6(request):
    questions = Question.objects.all()[25:30]
    responses_summary = []

    for question in questions:
        choices = question.choice_set.all()
        response_count = {}
        
        max_count = 0
        most_selected_choice_text = ''

        for choice in choices:
            count = Responses.objects.filter(question=question, choice=choice).count()
            response_count[choice.choice_text] = count
            
            if count > max_count:
                max_count = count
                most_selected_choice_text = choice.choice_text
        
        responses_summary.append({
            'question': question,
            'response_count': response_count,
            'most_selected_choice_text': most_selected_choice_text
        })

    return render(request, 'polls/thank_you6.html', {'responses_summary': responses_summary})

def SurveryCompleted(request):
    return render(request, 'polls/SurveryCompleted.html')