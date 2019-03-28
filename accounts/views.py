from django.shortcuts import render, HttpResponseRedirect
from sales.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
