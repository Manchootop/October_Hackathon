from django.urls import path

from Octomber_Hackathon.api.views import ListAdvocatesView

urlpatterns = (
    # path('', endpoints, name='endpoints'),
    
    path('advocates/', ListAdvocatesView.as_view(), name='list advocates'),
    # path('advocates/<str:id>/'),
    # path('companies/'),
    # path('companies/<str:id>'),
)
