from django.urls import path
from .views import cases_list, CaseCreateView, CaseUpdateView, track_case
from django.views.generic import TemplateView


app_name = "cases"

urlpatterns = [ 
    path("", cases_list, name="cases_list"),
    path('add/', CaseCreateView.as_view(), name='add_case'),
    path('<int:pk>/edit/', CaseUpdateView.as_view(), name='edit_case'),
    path('track-case/', track_case, name='track_case'),
]

