from django.urls import path
# from .views import 
from django.views.generic import TemplateView


app_name = "staff"

urlpatterns = [ 
    path("home/", TemplateView.as_view(template_name="staff_home.html")),
]

