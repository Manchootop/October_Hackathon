from django.http import Http404
from rest_framework import generics as api_generic_views, permissions

from Octomber_Hackathon.api.serializers import ListAdvocatesSerializer
from Octomber_Hackathon.auth_app.models import AdvocateProfile

'''
{
    "id":1,
    "name":"Dennis Ivy",
    "profile_pic":"/user_pic.png",
    "short_bio":"...",
    "long_bio":"...",
    "advocate_years_exp":1,
    "company":{
        "id":6,
        "name":"Agora",
        "logo":"agora_logo.png",
        "href":"/companies/6",
    },
    "links":{
        "youtube":"youtube.com/username",
        "twitter":"twitter.com/username",
        "github":"github.com/username",
    }
}
'''


class ListAdvocatesView(api_generic_views.ListAPIView):
    queryset = AdvocateProfile.objects.all()
    serializer_class = ListAdvocatesSerializer


