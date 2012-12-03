from django.shortcuts import render

def create (request):
    return render(request, 'elements/create.html')