from booking.utils import opus_render

import account.views
import musicians.forms

from account.decorators import login_required


def profile(request, slug=None):
    return opus_render(request, "musicians/profile.html")


@login_required
def dashboard(request):
    context = request.GET
    return opus_render(request, "musicians/dashboard.html", context)


@login_required
def editor(request):
    context = request.GET
    return opus_render(request, "musicians/editor.html", context)

@login_required
def venue_questions(request):
    return opus_render(request, "musicians/venue_questions.html")


@login_required
def settings(request):
    return opus_render(request, "musicians/settings.html")


class SignupView(account.views.SignupView):

    form_class = musicians.forms.SignupForm
    identifier_field = 'email'

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = "<magic>"
        return username
