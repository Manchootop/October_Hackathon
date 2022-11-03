from django.http import Http404, JsonResponse
from rest_framework import generics as api_generic_views, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response


from Octomber_Hackathon.api.serializers import ListAdvocatesSerializer, CreateAndEditAdvocateSerializer, \
    RetrieveAdvocateSerializer
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


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


class ListOrCreateAdvocateView(api_generic_views.ListCreateAPIView):
    queryset = AdvocateProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAndEditAdvocateSerializer
        return ListAdvocatesSerializer

    # query_filter_names = ('username', 'company')

    # /advocates/?name={username}&company={company}
    # def __apply_query_filters(self, queryset):
    #     filter_options = {}
    #     for filter_name in self.query_filter_names:
    #         value = self.request.query_params.get(filter_name, None)
    #         if value:
    #             filter_options[f'{filter_name}_id'] = value
    #
    #     return queryset.filter(**filter_options)
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     self.__apply_query_filters(queryset)
    #
    #     return queryset


class AdvocateDetailsView(api_generic_views.RetrieveAPIView):
    queryset = AdvocateProfile.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAndEditAdvocateSerializer
        return RetrieveAdvocateSerializer


