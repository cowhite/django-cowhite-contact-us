from django.core.management.base import BaseCommand, CommandError
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.conf import settings

from django_cowhite_contact_us.models import ContactUs

from datetime import datetime

class Command(BaseCommand):
    help = 'Send mail for every new instance to ContactUs model.'

    def handle(self, *args, **options):
        contacts = Contact.objects.filter(mail_sent=False)
        for contact in contacts:
            subject = render_to_string("django_cowhite_contact_us/contact_email_subject.txt")

            body = render_to_string("django_cowhite_contact_us/contact_email_body.html", {"obj": contact})
            send_mail(subject, "", html_message=body)
            contact.mail_sent = True
            contact.save()