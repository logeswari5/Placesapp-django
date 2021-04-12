from django.urls import path
from places import views


urlpatterns = [
    path('', views.index, name="index"),

    path('places/', views.PlaceListView.as_view(), name="places"),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name="place"),
       ]