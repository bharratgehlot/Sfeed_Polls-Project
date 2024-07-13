import os
import django
from django.utils import timezone

# Set up Django Environment 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sfeed_project.settings")
django.setup()

from polls.models import Question, Choice

questions_and_choice = [
  {
    "question_text": "How would you rate your teacher's knowledge of the subject?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "How well does your teacher cover the syllabus?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "How would you describe your teacher's behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "How effectively does your teacher address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "How would you rate your teacher's teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
  },
  {
    "question_text": "How often does your teacher use teaching aids (like presentations, videos, etc.) to enhance learning?",
    "choices": ["A. Frequently and effectively", "B. Occasionally, but they are helpful", "C. Rarely, and they are not very useful", "D. Never uses teaching aids"]
  },
  {
    "question_text": "Does your teacher encourage participation and discussion in class?",
    "choices": ["A. Always creates opportunities for students to participate", "B. Sometimes encourages participation, but it's not consistent", "C. Rarely encourages participation", "D. Never encourages participation"]
  },
  {
    "question_text": "How would you rate the overall learning environment in the class?",
    "choices": ["A. Stimulating and conducive to learning", "B. Generally positive, but could be improved", "C. Uninspiring and dull", "D. Hostile and unpleasant"]
  },
  {
    "question_text": "Does your teacher provide timely and constructive feedback on assignments and exams?",
    "choices": ["A. Provides clear and helpful feedback promptly", "B. Provides feedback, but it is sometimes unclear or delayed", "C. Rarely provides feedback", "D. Never provides feedback"]
  },
  {
    "question_text": "Overall, how satisfied are you with your teacher's performance?",
    "choices": ["A. Very satisfied", "B. Satisfied", "C. Dissatisfied", "D. Very dissatisfied"]
  }
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
    