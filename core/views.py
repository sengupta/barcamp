import datetime

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from .forms import RegisterForm, LoginForm
from .models import UserProfile, Camp

class HomeView(TemplateView):
    def get(self, request):
        self.template_name = "home.html"
        #TODO: Add login and registration forms to home page
        return self.render_to_response({})

    def post(self, request):
        pass

class RegisterView(TemplateView):
    template_name = "auth/register.html"
    def get(self, request):
        register_form = RegisterForm()
        return self.render_to_response({
                    'register_form': register_form,
                    })

    def post(self, request):
        register_form = RegisterForm(data=request.POST)
        if not register_form.is_valid():
            return self.render_to_response({
                'register_form': register_form
                })

        profile = register_form.save()

        user = authenticate(username=profile.user.username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('dashboard'))

class LoginView(TemplateView):
    template_name = "auth/login.html"
    def get(self, request):
        login_form = LoginForm()
        return self.render_to_response({
            'login_form': login_form
            })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return self.render_to_response({
                'login_form': login_form
                })
        user = login_form.user
        login(request, user)
        return HttpResponseRedirect(reverse('dashboard'))


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"
    def get(self, request):
        return self.render_to_response({})

    def post(self, request):
        pass

class CampListView(TemplateView):
    template_name="camp_list.html"
    def get(self, request):
        now = datetime.datetime.now()

        past_camps = Camp.objects.filter(end__lt=now)
        current_camps = Camp.objects.filter(start__gt=now, end__lt=now)
        upcoming_camps = Camp.objects.filter(start__gt=now)
        unscheduled_camps = Camp.objects.filter(start=None, end=None)

        return self.render_to_response({
            'past': past_camps,
            'present': current_camps,
            'future': upcoming_camps,
            'unknown': unscheduled_camps,
            })

    def post(self, request):
        pass
class CampView(TemplateView):
    template_name="camp.html"
    def get(self, request, camp_slug):
        try:
            camp = Camp.objects.get(slug=camp_slug)
        except:
            raise Http404
        return self.render_to_response({
            'camp': camp,
            })

    def post(self, request):
        pass

class SessionView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class SessionCreateView(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        pass

class SessionEditView(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        pass

class ProfileView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class ProfileCreateView(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        pass

class ProfileEditView(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        pass

