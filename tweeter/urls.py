from django.urls import path, include

from . import views

urlpatterns = [
    path('tweet/', views.TweetListCreateAPIView.as_view()),
    path('comment/', views.CommentListCreateAPIView.as_view()),
    path('mark/', views.MarkListCreateAPIView.as_view()),
]
