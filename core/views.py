from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import RegisterForm
from .models import UserProfile

class HomeView(TemplateView):
    def get(self, request):
        self.template_name = "home.html"
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
        data = register_form.cleaned_data
        name = data['name']
        email = data['email']
        password = data['password']

        profile=UserProfile.profiles.create_profile(
                name=name,
                email=email,
                password=password
                )
        user = authenticate(username=profile.user.username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('dashboard'))

    def post(self, request):
        pass

class RegisterView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CampView(TemplateView):
    def get(self, request):
        pass

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

