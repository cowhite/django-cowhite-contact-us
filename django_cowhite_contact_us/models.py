from django.db import models


class DateTimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactUs(DateTimeBase):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    mail_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.name