from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('composerindex')
    else:
        form = UserRegisterForm()
    return render(request, 'students/register.html', {'form': form})
    
def login(request):
    return render(request, "students/login.html")