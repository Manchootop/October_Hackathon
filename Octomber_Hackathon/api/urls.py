from django.urls import path

from Octomber_Hackathon.api import views

urlpatterns = [
    path('', views.endpoints, name='endpoints'),

    path('advocates/', views.ListOrCreateAdvocateView.as_view(), name='list or create an advocate'),
    path('advocates/<str:username>/', views.AdvocateRetrieveUpdateDestroyView.as_view(),
         name='get or update or delete an advocate'),

    path('company/', views.CompanyListCreateView.as_view(), name='list or create a company'),
    path('company/<str:name>/', views.CompanyRetrieveUpdateDestroyView.as_view(),
         name='get or update or delete a company')
]
