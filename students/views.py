from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You account has been created! You can log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'students/register.html', {'form': form})
