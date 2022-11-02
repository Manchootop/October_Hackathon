from django.db import models


class Companies(models.Model):
    COMPANY_MAX_LENGTH = 25

    name = models.CharField(
        max_length=COMPANY_MAX_LENGTH
    )

    logo = models.ImageField()

    summary = models.TextField()

    def __str__(self):
        return f'{self.name}'
