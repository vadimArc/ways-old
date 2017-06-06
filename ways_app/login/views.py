from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.models import User

from login.models import Profile, Cities, Lists, Cache, Places
from .forms import UserForm, CitySearch, ListAdd, PlaceAdd, PlaceSave, FindFriends
from .decorators import profile_exists
from .fsq_auth import client
from .fsq_search import city_search, venue_query_search, venue_save

def index(request):
    return render(request, 'home.html')

def home(request):
    # current_user = request.user
    # if current_user.is_authenticated:
    #     if hasattr(current_user, 'profile'):
    #         return render(request, 'profile.html', {'profile': Profile.objects.first()})
    return render(request, 'home.html')

def register_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            user_data = Profile(
                first_name = name,
                last_name = last_name,
                username = username,
                email = email,
                user = request.user
            )

            user_data.save()
            # redirect to a new URL:
            return redirect('profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'user_info.html', {'form': form})

@login_required
@profile_exists
def profile(request):
    #add profile from current user
    user = request.user.profile
    return render(request, 'profile.html', {'profile': user})

@login_required
@profile_exists
def city_add(request):

    user_cities = request.user.profile.cities_set.all()

    if request.method == 'POST':
        form = CitySearch(request.POST)
        if form.is_valid():
            query = form.cleaned_data['city']
            user = request.user.profile
            results = city_search(query)
            city = results['city']
            country = results ['country']
            city_data = Cities (
                city = city,
                country= country,
            )
            city_data.save()
            user.cities_set.add(city_data)
            return render(request, 'cities.html', {'form': form, 'user_cities': user_cities})
    else:
        form = CitySearch()
    return render(request, 'cities.html', {'form': form, 'user_cities': user_cities})

@login_required
@profile_exists
def add_list(request, city_name):
    if request.method == 'POST':
        form = ListAdd(request.POST)
        if form.is_valid():
            list_name = form.cleaned_data['list_name']
            user = request.user.profile
            city = Cities.objects.filter(city = city_name).first()
            list_data = Lists(
                name = list_name,
                owner = user,
                city = city
            )
            list_data.save()
            return redirect(user_places, city_name=city_name)
    else:
        form = ListAdd()
    return render(request, 'add_list.html', {'form': form, 'city_name':city_name })

@login_required
@profile_exists
def user_places(request, city_name):
    user_city = request.user.profile.cities_set.filter(city=city_name).first()
    user_list = user_city.lists_set.first()
    if request.method == 'POST':
        form = PlaceAdd(request.POST)
        if form.is_valid():
            found_venues = venue_query_search(
                query = form.cleaned_data['place_name'],
                city = user_city.city
            )
            return render(request, 'places_search_results.html', {'city_name':city_name, 'venues':found_venues, 'form':PlaceSave()})
    else:
        form = PlaceAdd()
    return render(request, 'places.html', {'user_list': user_list, 'user_city': user_city, 'form': form})

@login_required
@profile_exists
def add_place(request, city_name, venue_id):
    if request.method == 'POST':
        form = PlaceSave(request.POST)
        if form.is_valid():
            venue_info = venue_save(venue_id, city_name)
            user = request.user.profile
            city = user.cities_set.filter(city=city_name).first()
            list = city.lists_set.first()
            list.places_set.add(venue_info)
            return redirect(user_places, city_name = city_name)

@login_required
@profile_exists
def user_friends(request):
    user = request.user.profile
    if request.method == 'POST':
        form = FindFriends(request.POST)
        if form.is_valid():
            query = form.cleaned_data['username']
            results = Profile.objects.filter(username=query).first()
            results.profile_set.add(user)
            return render(request, 'friends.html', {'user': user, 'form': form})
    else:
        form = FindFriends()
    return render(request, 'friends.html', {'user': user, 'form': form})
