from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('subject1/', views.subject1, name='subject1'),
    path('submit1/', views.submit1, name="submit1"),
    path('thank_you1/<int:user_id>/', views.thank_you1, name='thank_you1'),
    path('subject2/', views.subject2, name='subject2'),
    path('submit2/', views.submit2, name='submit2'),
    path('thank_you2/<int:user_id>/', views.thank_you2, name='thank_you2'),
    path('subject3/', views.subject3, name='subject3'),
    path('submit3/', views.submit3, name='submit3'),
    path('thank_you3/<int:user_id>/', views.thank_you3, name='thank_you3'),
    path('subject4/', views.subject4, name='subject4'),
    path('submit4/', views.submit4, name='submit4'),
    path('thank_you4/<int:user_id>/', views.thank_you4, name='thank_you4'),
    path('subject5/', views.subject5, name='subject5'),
    path('submit5/', views.submit5, name='submit5'),
    path('thank_you5/<int:user_id>/', views.thank_you5, name='thank_you5'),
    path('subject6/', views.subject6, name='subject6'),
    path('submit6/', views.submit6, name='submit6'),
    path('thank_you6/<int:user_id>/', views.thank_you6, name='thank_you6'),
    path('survey_completed/', views.survey_completed, name='survey_completed'),
    path('clginfra/', views.clginfra, name='clginfra'),
]
