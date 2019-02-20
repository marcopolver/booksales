from django.shortcuts import render

# Create your views here.

#View relativa ad homepage
def home(request):
    return render(request, 'home_page.html')
