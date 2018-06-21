from django import forms
from django.conf import settings

from .models import ContactUs

import requests


class ContactForm(forms.ModelForm):
    captcha = forms.CharField(required=False)

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'message', 'captcha')

    def clean(self, *args, **kwargs):
        cleaned_data = super(ContactForm, self).clean(*args, **kwargs)
        if not self.is_valid():
            return cleaned_data

        if "g-recaptcha-response" not in self.data:
            errors = self._errors.setdefault("captcha", self.error_class())
            errors.append("Please enter captcha.")
            return cleaned_data

        captcha = self.data["g-recaptcha-response"]
        if not captcha:

            errors = self._errors.setdefault("captcha", self.error_class())
            errors.append("Please enter captcha.")
            return cleaned_data

        url = "https://www.google.com/recaptcha/api/siteverify"
        r = requests.post(
            url,
            data={
                "secret": settings.CAPTCHA_SECRET,
                "response": captcha})
        wrong_captcha = False
        if "success" not in r.json():
            wrong_captcha = True
        else:
            if not r.json()["success"]:
                wrong_captcha = True
        if wrong_captcha:
            errors = self._errors.setdefault("captcha", self.error_class())
            errors.append("Invalid captcha.")
        return cleaned_data
