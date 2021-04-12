from django.urls import path
from places import views


urlpatterns = [
    path('', views.index, name="index"),

    path('places/', views.PlaceListView.as_view(), name="places"),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name="place"),
    path('sortcity/', views.sortcity, name="sort_by_city"),

    path('distinct_cities/<str:cityname>', views.all_place_in_city, name="instance-city-place"),
]
