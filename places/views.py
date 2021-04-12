from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from places.models import Place
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'places/index.html')




class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'places/place.html'
    context_object_name = 'place'
    paginate_by = 2
    queryset = Place.objects.filter(location__isnull=False)



class PlaceListView(generic.ListView):
    model = Place
    template_name = 'places/places.html'
    context_object_name = 'places'
    paginate_by = 2
    queryset = Place.objects.filter(location__isnull=False)

class PlaceCreate(generic.CreateView):
    model = Place
    fields = ['title', 'location', 'description', 'address', 'phone', 'city', 'type_of_place']
    template_name = 'places/add_places.html'
