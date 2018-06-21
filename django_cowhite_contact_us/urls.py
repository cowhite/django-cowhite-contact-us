from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import ContactView


urlpatterns = [
    url(r'^$', ContactView.as_view(), name="contact-us"),
    url(r'^success/$', TemplateView.as_view(template_name="django_cowhite_contact_us/success.html")),
]
