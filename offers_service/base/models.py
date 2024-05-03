from django.db import models


# Create your models here.
class Offer(models.Model):

    STATES = {
        "PENDING": "PENDING",
        "ACCEPTED": "ACCEPTED",
        "REJECTED": "REJECTED"
    }
    state = models.CharField(max_length=30, choices=STATES.items(), default="PENDING")
    is_signed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    request_id = models.CharField(max_length=255)
