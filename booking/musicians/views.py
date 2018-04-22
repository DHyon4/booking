from django.conf import settings as conf_settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from booking.utils import opus_render
from account.decorators import login_required
import account.views

import random
import string

from .models import Musician
from .forms import SignupForm, MusicianForm


def profile(request, slug=None):

    musician = get_object_or_404(Musician, slug=slug)

    print(musician.user.facebook_followers())

    context = {
        "musician": musician,
    }

    return opus_render(request, "musicians/profile.html", context)


@login_required
def social(request):

    # TODO: set up a better way of listing social integrations based on existing context_processor
    #   https://github.com/python-social-auth/social-app-django/blob/master/social_django/context_processors.py
    # from social_core.backends.utils import user_backends_data
    # from social_django.utils import Storage, BACKENDS

    # print(BACKENDS)
    # print(user_backends_data(request.user, BACKENDS, Storage))


    all_socials = {
        'instagram': {},
        'facebook': {},
        'spotify': {},
    }

    for social in all_socials.keys():
        if request.user.social_auth.filter(provider=social).exists():
            all_socials[social]['social_auth'] = request.user.social_auth.get(provider=social)

    context = {
        "all_socials": all_socials,
    }

    return opus_render(request, "musicians/social.html", context)


@login_required
def dashboard(request):

    musician = None

    if Musician.objects.filter(user=request.user).exists():
        musician = Musician.objects.get(user=request.user)

    context = {
        "applied": request.GET.get('applied'),
        "musician": musician,
        "profile_created": musician
    }
    return opus_render(request, "musicians/dashboard.html", context)


@login_required
def editor(request):

    musician = None

    if Musician.objects.filter(user=request.user).exists():
        musician = Musician.objects.get(user=request.user)
        if request.POST or request.FILES:
            form = MusicianForm(request.POST, request.FILES, instance=musician)
        else:
            form = MusicianForm(instance=musician)
    else:
        form = MusicianForm(request.POST, request.FILES)

    if form.is_valid():
        musician = form.save(commit=False)
        musician.user = request.user
        musician.save()

        # Show a success message
        messages.success(request, 'Profile details updated. Yay.')

        # redirect to same page, to avoid the stupid repost issue
        redirect('musician_dash')

    context = {
        'form': form,
        'musician': musician,
        'apptype': request.GET.get('apptype')
    }
    return opus_render(request, "musicians/editor.html", context)


@login_required
def venue_questions(request):
    return opus_render(request, "musicians/venue_questions.html")


@login_required
def settings(request):
    return opus_render(request, "musicians/settings.html")


class SignupView(account.views.SignupView):

    form_class = SignupForm
    identifier_field = 'email'

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        return form.data['email']


    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)


    def update_profile(self, form):
        self.created_user.is_musician = True
        self.created_user.save()

