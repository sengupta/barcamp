import datetime

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory

from .forms import RegisterForm, LoginForm, SessionForm
from .models import UserProfile, Camp, Session

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
        next = request.GET.get('next')
        register_form = RegisterForm(initial={'next': next})
        return self.render_to_response({
                    'register_form': register_form,
                    'next': next,
                    })

    def post(self, request):
        register_form = RegisterForm(data=request.POST)
        if not register_form.is_valid():
            return self.render_to_response({
                'register_form': register_form
                })

        profile = register_form.save()

        user = authenticate(
                username=profile.user.username,
                password=register_form.cleaned_data['password']
                )
        login(request, user)
        redirect = request.POST.get('next', reverse('dashboard'))
        return HttpResponseRedirect(redirect)

class LoginView(TemplateView):
    template_name = "auth/login.html"
    def get(self, request):
        next = request.GET.get('next')
        login_form = LoginForm(initial={'next': next})
        return self.render_to_response({
            'login_form': login_form,
            'next': next,
            })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return self.render_to_response({
                'login_form': login_form
                })
        user = login_form.user
        login(request, user)
        redirect = request.POST.get('next', reverse('dashboard'))
        return HttpResponseRedirect(redirect)

class DashboardView(TemplateView):
    template_name = "dashboard/index.html"
    @method_decorator(login_required)
    def get(self, request):
        sessions = request.user.profile.sessions.all()
        return self.render_to_response({'sessions': sessions})

    @method_decorator(login_required)
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
    def get(self, request, camp):
        try:
            camp = Camp.objects.prefetch_related('sessions').get(slug=camp)
        except:
            raise Http404
        return self.render_to_response({
            'camp': camp,
            'sessions': camp.sessions.all(),
            })

    def post(self, request):
        pass

class SessionView(TemplateView):
    template_name = "session/view.html"
    def get(self, request, camp, session):
        try:
            session = Session.objects\
                        .select_related('camp')\
                        .get(slug=session)
            if not session.camp.slug == camp:
                raise Http404("This session is in another camp")
        except Session.DoesNotExist:
            raise Http404("Session does not exist")
        return self.render_to_response({
            'camp': session.camp,
            'session': session
            })

    def post(self, request):
        pass

class SessionCreateView(TemplateView):
    template_name = "session/create.html"
    @method_decorator(login_required)
    def get(self, request, camp):
        form = SessionForm()
        return self.render_to_response({
            'form': form,
            'mode': 'create'
            })

    @method_decorator(login_required)
    def post(self, request, camp):
        try:
            camp = Camp.objects.get(slug=camp)
        except:
            raise Http404
        # TODO: If camp is in the past, raise error
        form = SessionForm(request.POST)
        session = form.save(commit=False)
        session.camp = camp
        session.speaker = request.user.get_profile()
        session.save()
        return HttpResponseRedirect(
            reverse("session_view", kwargs={
                'camp': camp.slug,
                'session': session.slug,
                })
            )

class SessionEditView(TemplateView):
    template_name = "session/create.html"
    @method_decorator(login_required)
    def get(self, request, camp, session):
        try:
            camp = Camp.objects.get(slug=camp)
            session = Session.objects.get(
                    camp=camp,
                    slug=session,
                    speaker=request.user.get_profile()
                    )
        except:
            raise Http404
        form = SessionForm(instance=session)
        return self.render_to_response({
            'form': form,
            'mode': 'edit'
            })

    @method_decorator(login_required)
    def post(self, request, camp, session):
        try:
            camp = Camp.objects.get(slug=camp)
            session = Session.objects.get(
                    camp=camp,
                    slug=session,
                    speaker=request.user.get_profile()
                    )
        except:
            raise Http404
        form = SessionForm(instance=session, data=request.POST)
        session = form.save()
        return HttpResponseRedirect(
            reverse("session_view", kwargs={
                'camp': camp.slug,
                'session': session.slug,
                })
            )

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

