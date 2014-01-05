from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    def get(self):
        pass

    def post(self):
        pass

class LoginView(TemplateView):
    def get(self):
        pass

    def post(self):
        pass

class RegisterView(TemplateView):
    def get(self):
        pass

    def post(self):
        pass

class CampView(TemplateView):
    def get(self):
        pass

    def post(self):
        pass

class SessionView(TemplateView):
    def get(self):
        pass

    def post(self):
        pass

class SessionCreateView(TemplateView):
    @method_decorator(login_required)
    def get(self):
        pass

    @method_decorator(login_required)
    def post(self):
        pass

class SessionEditView(TemplateView):
    @method_decorator(login_required)
    def get(self):
        pass

    @method_decorator(login_required)
    def post(self):
        pass

class ProfileView(TemplateView):
    def get(self):
        pass

    def post(self):
        pass

class ProfileCreateView(TemplateView):
    @method_decorator(login_required)
    def get(self):
        pass

    @method_decorator(login_required)
    def post(self):
        pass

class ProfileEditView(TemplateView):
    @method_decorator(login_required)
    def get(self):
        pass

    @method_decorator(login_required)
    def post(self):
        pass

