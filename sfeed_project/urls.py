from django.contrib import admin
from django.urls import path, include
from polls.views import home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include(('polls.urls', 'polls'), namespace='polls')),
    path("", home_page, name="home"),
]
