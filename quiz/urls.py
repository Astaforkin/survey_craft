from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='quiz-home'),
	path('polls/', views.polls, name='polls-tests'),
	path('polls/<int:poll_id>/', views.detail, name='detail'),
	path('polls/<int:poll_id>/questions/',views.questions, name='questions-tests'),
	path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
]
