from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from login.models import Profile


def profile_exists(function):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated:
            if not hasattr(current_user, 'profile'):
                return redirect('home')
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
