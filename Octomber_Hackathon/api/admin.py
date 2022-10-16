from django.contrib import admin
from Octomber_Hackathon.api import models as api_models
from Octomber_Hackathon.auth_app import models as auth_models


@admin.register(api_models.Companies)
class CompaniesAdmin(admin.ModelAdmin):
    pass
