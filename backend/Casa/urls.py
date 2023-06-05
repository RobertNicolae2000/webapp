from django.urls import path

from Casa import views

urlpatterns = [
    path('case/', views.CasaList.as_view()),
    path('case/search/', views.search),
    path('case/<slug:casa_slug>/', views.CasaDetail.as_view()),
    path('adaugarecasa/', views.CasaList.as_view()),
]