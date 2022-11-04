from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('discuss', views.ContactFormView.as_view(), name="discuss"),
    path('responsebot/',
         TemplateView.as_view(template_name="response.html"), name="reponse")
]
