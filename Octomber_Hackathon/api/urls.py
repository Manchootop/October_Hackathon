from django.urls import path

from Octomber_Hackathon.api import views

urlpatterns = (
    path('', views.endpoints, name='endpoints'),
    
    path('advocates/', views.ListOrCreateAdvocateView.as_view(), name='list advocates'),
    path('advocates/<str:username>/', views.AdvocateDetailsView.as_view(), name='details advocate'),

    # path('companies/'),
    # path('companies/<str:id>'),
)
