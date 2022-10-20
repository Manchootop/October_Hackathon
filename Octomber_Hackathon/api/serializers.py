from rest_framework import serializers

from Octomber_Hackathon.auth_app.models import AdvocateProfile


class ListAdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateProfile
        exclude = ('user',)
