from django.urls import path
from .views import RecNamesListCreateView,RecNamesRetrieveUpdateDestroyView

urlpatterns=[
    path('recnames/', RecNamesListCreateView.as_view(), name='recnames-list-create'),
    path('recnames/<int:pk>/', RecNamesRetrieveUpdateDestroyView.as_view(), name='recnames-detail')
]