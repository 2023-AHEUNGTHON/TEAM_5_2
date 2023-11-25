from django.urls import path

from .views import WordcloudView, WordView

urlpatterns = [
    path('', WordcloudView.as_view()),
    path('<str:pk>/', WordView.as_view()),
]