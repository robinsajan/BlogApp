from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def LoginView(request):
    if request.method == "POST":
        form = CustomUserAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            User = get_user_model().objects.get(email=email)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid Credentials")

        else:
            messages.warning(request, "Enter All the Credentials")
    else:
        form = CustomUserAuthenticationForm()

    return render(request, 'login.html', {"form": form})


def LogoutView(request):
    logout(request)
    return redirect('home')


def CreateUserView(request):
    if request.method == "POST":
        form = CustomUserCreationForm()

        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = request.POST['name']
        try:
            user_exist = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            user_exist = False
        if (not user_exist):
            if len(password1) > 8:
                if password1 == password2:
                    if not any(char.isdigit() for char in password1):
                        messages.warning(
                            request, "password should have atleast one numeric value")
                    else:
                        get_user_model().objects.create_user(
                            email, password1, name)
                        return redirect('login')
                else:
                    messages.warning(
                        request, "passwords dont match")
            else:
                messages.warning(
                    request, "Password too small")
        else:
            messages.warning(
                request, "User already exists")
    else:
        form = CustomUserCreationForm()
    try:
        super_user = get_user_model().objects.get(is_superuser=True)

    except get_user_model().DoesNotExist:
        super_user = False
    print(super_user)
    context = {
        'form': form,
        'super_user': super_user,
    }
    return render(request, 'create_viewer.html', context)


def CreateAuthorView(request):
    if request.method == "POST":
        form = CustomUserCreationForm()

        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = request.POST['name']
        try:
            user_exist = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            user_exist = False
        print(user_exist)
        if (not user_exist):
            if len(password1) > 8:
                if password1 == password2:
                    if not any(char.isdigit() for char in password1):
                        messages.warning(
                            request, "password should have atleast one numeric value")
                    else:
                        get_user_model().objects.create_superuser(
                            email, password1, name)
                        user = authenticate(
                            request, email=email, password=password1)
                        login(request, user)
                        return redirect('add-profile')
                else:
                    # messages.add_message(request, level, message, extra_tags='', fail_silently=False)
                    messages.warning(
                        request, "passwords dont match")
            else:
                messages.warning(
                    request, "Password too small")
        else:
            messages.warning(
                request, "User already exists")
    else:
        form = CustomUserCreationForm()
    try:
        super_user = get_user_model().objects.get(is_superuser=True)
    except get_user_model().DoesNotExist:
        super_user = False
    print(super_user)
    context = {
        'form': form,
        'super_user': super_user,
    }
    return render(request, 'create_author.html', context)
