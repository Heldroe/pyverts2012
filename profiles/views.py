from django.shortcuts import render

def my_profile (request):
    return render(request, 'my_profile.html')