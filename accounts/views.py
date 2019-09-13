from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.tokens import account_activation_token
from .forms import LoginForm, RegisterForm, ProfileUpdateFrom, UserUpdateForm

User = get_user_model()


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
            'title': 'login',
            'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data['username'].lower()
        password = form.cleaned_data['password'].lower()
        user = authenticate(request, username=username, password=password,
                            )
        if user:
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            context['form'] = LoginForm()
            context['user'] = username
            return redirect('books:home')

    return render(request, "login.html", context=context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
            'title': 'register',
            'form': form
    }
    if form.is_valid():
        username = form.cleaned_data['username'].lower()
        password = make_password(form.cleaned_data['password'].lower())
        email = form.cleaned_data['email'].lower()
        first_name = form.cleaned_data['first_name'].lower()
        last_name = form.cleaned_data['last_name'].lower()
        user = User.objects.create(username=username, password=password, email=email, first_name=first_name,
                                   last_name=last_name)
        user.is_active = False
        current_site = get_current_site(request)
        subject = 'Activate Your MySite Account'
        message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return redirect('account_activation_sent')
    return render(request, "register.html", context=context)


def logout_page(request):
    logout(request=request)
    return redirect('books:home')


@login_required
def profile(request):
    if request.method == "POST":
        pu_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        up_form = UserUpdateForm(request.POST, instance=request.user)

        if pu_form.is_valid() and up_form.is_valid():
            pu_form.save()
            up_form.save()
            return redirect('account:profile')
    else:
        pu_form = ProfileUpdateFrom(instance=request.user.profile)
        up_form = UserUpdateForm(instance=request.user)

    context = {
            "pu_form": pu_form,
            "up_form": up_form

    }
    return render(request, 'profile.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect('books:home')
    else:
        return render(request, 'account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')
