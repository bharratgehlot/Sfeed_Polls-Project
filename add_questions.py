import os
import django
from django.utils import timezone

# Set up Django Environment 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sfeed_project.settings")
django.setup()

from polls.models import Question, Choice

questions_and_choice = [
  {
    "question_text": "1. How would you rate your teacher's knowledge of the python subject?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "2. How well does your teacher cover the syllabus python ?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "3. How would you describe your teacher's behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "4. How effectively does your mam address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "5. How would you rate your mam's teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
  },
  
   {
    "question_text": "1. How would you rate your teacher's knowledge of the maths subject?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "2. How well does your teacher cover the syllabus in maths ?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "3. How would you describe your teacher's behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "4. How effectively does your sir address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "5. How would you rate your sir's teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
  },
  
   {
    "question_text": "1. How would you rate your teacher's knowledge of the DCS subject?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "2. How well does your teacher cover the syllabus DCS ?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "3. How would you describe your teacher's behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "4. How effectively does your teacher address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "5. How would you rate your his teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
  },
    {
    "question_text": "1. How would you rate your teacher's knowledge of the environmental studies?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "2. How well does your teacher cover the syllabus ?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "3. How would you describe your teacher's behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "4. How does your SIR address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "5. How would you rate your Teacher's teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
  },
  
   {
    "question_text": "1. How would you rate your teacher's knowledge of the ETW subject?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "2. How well does your teacher cover the syllabus in ETW ?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "3. How would you describe your teacher's behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "4. How effectively does your madam address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "5. How would you rate your madam teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
  },
  
   {
    "question_text": "1. How would you rate your teacher's knowledge of the Web developmet ?",
    "choices": ["A. Excellent: Has a deep understanding and can explain complex concepts clearly.", "B. Good: Has a strong grasp of the subject matter and can answer most questions.", "C. Average: Possesses basic knowledge but struggles with in-depth explanations.", "D. Poor: Lacks sufficient subject knowledge and often provides incorrect information."]
  },
  {
    "question_text": "2. How well does your teacher cover the syllabus ?",
    "choices": ["A. Excellent: Covers the entire syllabus in depth and on time.", "B. Good: Covers most of the syllabus but may rush through some topics.", "C. Average: Covers the main points but misses some important details.", "D. Poor: Does not cover the required syllabus adequately."]
  },
  {
    "question_text": "3. How would you describe your sitaram's sir behavior towards students?",
    "choices": ["A. Excellent: Supportive, encouraging, and approachable.", "B. Good: Generally positive but can be strict at times.", "C. Average: Indifferent and shows little interest in students.", "D. Poor: Rude, impatient, and disrespectful towards students."]
  },
  {
    "question_text": "4. How effectively does your teacher address students' doubts?",
    "choices": ["A. Excellent: Patiently explains concepts until students understand.", "B. Good: Tries to help but sometimes struggles to clarify doubts.", "C. Average: Only answers easy questions and avoids complex ones.", "D. Poor: Shows impatience and reluctance to answer questions."]
  },
  {
    "question_text": "5. How would you rate his teaching ability?",
    "choices": ["A. Excellent: Engaging, inspiring, and makes the subject interesting.", "B. Good: Teaches clearly but lacks enthusiasm.", "C. Average: Relies heavily on textbooks and notes.", "D. Poor: Unable to explain concepts clearly and loses students' attention."]
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
    