from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice, User, Responses
import uuid

def home_page(request):
    return render(request, 'polls/home_page.html')

def subject(request, start, end, template_name):
    question_list = Question.objects.all()[start:end]
    context = {'questions': question_list}
    return render(request, f'polls/{template_name}', context)

def subject1(request):
    return subject(request, 0, 5, 'subject1.html')

def subject2(request):
    return subject(request, 5, 10, 'subject2.html')

def subject3(request):
    return subject(request, 10, 15, 'subject3.html')

def subject4(request):
    return subject(request, 15, 20, 'subject4.html')

def subject5(request):
    return subject(request, 20, 25, 'subject5.html')

def subject6(request):
    return subject(request, 25, 30, 'subject6.html')

def submit(request, user, start, end, thank_you_url):
    for question in Question.objects.all()[start:end]:
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            response = Responses(user=user, question=question, choice=choice)
            response.save()
    return redirect(thank_you_url, user_id=user.id)

def submit1(request):
    user, created = User.objects.get_or_create(username=str(uuid.uuid4()))
    request.session['user_id'] = user.id
    return submit(request, user, 0, 5, 'polls:thank_you1')

def submit2(request):
    user = get_object_or_404(User, pk=request.session.get('user_id'))
    return submit(request, user, 5, 10, 'polls:thank_you2')

def submit3(request):
    user = get_object_or_404(User, pk=request.session.get('user_id'))
    return submit(request, user, 10, 15, 'polls:thank_you3')

def submit4(request):
    user = get_object_or_404(User, pk=request.session.get('user_id'))
    return submit(request, user, 15, 20, 'polls:thank_you4')

def submit5(request):
    user = get_object_or_404(User, pk=request.session.get('user_id'))
    return submit(request, user, 20, 25, 'polls:thank_you5')

def submit6(request):
    user = get_object_or_404(User, pk=request.session.get('user_id'))
    return submit(request, user, 25, 30, 'polls:thank_you6')

def thank_you(request, user_id, start, end, template_name):
    user = get_object_or_404(User, pk=user_id)
    questions = Question.objects.all()[start:end]
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

    return render(request, f'polls/{template_name}', {'responses_summary': responses_summary})

def thank_you1(request, user_id):
    return thank_you(request, user_id, 0, 5, 'thank_you1.html')

def thank_you2(request, user_id):
    return thank_you(request, user_id, 5, 10, 'thank_you2.html')

def thank_you3(request, user_id):
    return thank_you(request, user_id, 10, 15, 'thank_you3.html')

def thank_you4(request, user_id):
    return thank_you(request, user_id, 15, 20, 'thank_you4.html')

def thank_you5(request, user_id):
    return thank_you(request, user_id, 20, 25, 'thank_you5.html')

def thank_you6(request, user_id):
    return thank_you(request, user_id, 25, 30, 'thank_you6.html')
  
def survey_completed(request):
    return render(request, 'polls/survey_completed.html')

def clginfra(request):
    return render(request, 'polls/clginfra.html')
