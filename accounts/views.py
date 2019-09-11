from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
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
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            context['form'] = LoginForm()
            context['user'] = username
            messages.success(request, "{} logged in successfully".format(username))
            return redirect('books:home')
        else:
            messages.error(request, "Please Enter Correct Credentials !!")

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
        context['user'] = user.username
        context['form'] = RegisterForm()
        messages.success(request, "User Registration Successful try to login with {}".format(context['user']))
        return redirect('account:login')
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
            messages.success(request, f'Your Account Has been Updated ')
            return redirect('account:profile')
    else:
        pu_form = ProfileUpdateFrom(instance=request.user.profile)
        up_form = UserUpdateForm(instance=request.user)

    context = {
            "pu_form": pu_form,
            "up_form": up_form

    }
    return render(request, 'profile.html', context)
