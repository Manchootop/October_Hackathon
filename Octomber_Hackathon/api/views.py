from django.http import Http404, JsonResponse
from rest_framework import generics as api_generic_views, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Octomber_Hackathon.api.models import Companies
from Octomber_Hackathon.api.serializers import AdvocateListSerializer, AdvocateCreateSerializer, \
    CompanySerializer, CompanyRetrieveUpdateDestroySerializer, \
    AdvocateUpdateDestroySerializer, AdvocateRetrieveSerializer
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
        "twitter_link":"twitter_link.com/username",
        "github":"github.com/username",
    }
}
'''


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates/', '/advocates/:username', '/advocates/?search=username'] + ['company/', 'company/:name'] + [
        '/login/', '/register/', 'logout'
    ]

    return Response(data)


class ListOrCreateAdvocateView(api_generic_views.ListCreateAPIView):
    # queryset = AdvocateProfile.objects.all()
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AdvocateCreateSerializer
        return AdvocateListSerializer

    # query_filter_names = ('username')

    # # /advocates/?name={username}&company={company}
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

    def get_queryset(self):

        queryset = AdvocateProfile.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(company__advocateprofile__username=username)
        return queryset


class AdvocateRetrieveUpdateDestroyView(api_generic_views.RetrieveUpdateDestroyAPIView):
    queryset = AdvocateProfile.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdvocateRetrieveSerializer
        else:
            return AdvocateUpdateDestroySerializer


class CompanyListCreateView(api_generic_views.ListCreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyView(api_generic_views.RetrieveUpdateDestroyAPIView):
    queryset = Companies
    serializer_class = CompanyRetrieveUpdateDestroySerializer
    lookup_field = 'name'
