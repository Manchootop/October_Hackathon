from django.db import models

from Octomber_Hackathon.auth_app.models import AdvocateProfile


class Companies(models.Model):
    COMPANY_MAX_LENGTH = 25

    name = models.CharField(
        max_length=COMPANY_MAX_LENGTH
    )

    logo = models.ImageField()

    summary = models.TextField()

    advocates = models.ManyToManyField(AdvocateProfile)

