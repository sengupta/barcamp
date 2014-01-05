from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    def get(self, request):
        self.template_name = "home.html"
        return self.render_to_response({})

    def post(self, request):
        pass

class LoginView(TemplateView):
    def get(self, request):
        pass

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

