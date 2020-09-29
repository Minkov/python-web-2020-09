from django.shortcuts import render


def landing_page(request):
    return render(request, 'index.html')

def original(request):
    return render(request, 'landing_page.html')
