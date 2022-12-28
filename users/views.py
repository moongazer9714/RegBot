from django.shortcuts import render, redirect
from .forms import CustomUserModelForm

def sign_up(request):
    form = CustomUserModelForm()
    if request.method == "POST":
        form = CustomUserModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register')
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
