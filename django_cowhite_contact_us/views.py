from django.shortcuts import render
from django.views.generic.edit import FormView
from django.conf import settings

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = "django_cowhite_contact_us/contact.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FormView, self).get_context_data(*args, **kwargs)
        context['CAPTCHA_KEY'] = settings.CAPTCHA_KEY
        return context

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse("django-cowhite-contact-us:success")