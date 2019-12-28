from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

user = get_user_model()


def register_view(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # username = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})



def register_complete_view(request):

    return render(request, 'users/register_complete.html')

