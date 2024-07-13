import os
import django
from django.utils import timezone

# Set up Django Environment 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polls_project.settings")
django.setup()

from polls.models import Question, Choice

questions_and_choice = [
  
    {
        "question_text": "21. When using Django ModelForms, what is the purpose of the cleaned_data dictionary?",
        "choices": ["A. It stores the raw form data submitted by the user.","B. It contains the validated and processed form data after cleaning.","C. It defines the layout and fields of the form in the template.","D. It manages the authorization rules for accessing model instances."]
    },

    {
        "question_text": "22. Within a Django template, how can you iterate over a list of objects retrieved from the context?",
        "choices": [
        "A. Using a standard for loop with the object list directly.",
        "B. Employing a custom template tag specifically designed for iteration.",
        "C. Accessing objects one by one using their index within the context.",
        "D. Django templates don't support looping through context data."]
        },

]

for items in questions_and_choice:
  question = Question.objects.create(
    question_text=items["question_text"],
    pub_date=timezone.now()
  )
  
  for choices in items["choices"]:
    Choice.objects.create(
      question=question,
      choice_text=choices,
      votes=0
    )
    
print("Questions and choices added successfully!")   
    