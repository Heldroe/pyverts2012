from django.shortcuts import render
from actstream.models import actor_stream, user_stream

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from haystack.query import SearchQuerySet

def home (request):
    if request.user.is_authenticated():
        u_stream = user_stream(request.user)
        return render(request, 'user_home.html', {'home': True, 'user_stream': u_stream})
    else:
        return render(request, 'home.html', {'home': True})

@csrf_exempt
def search (request):
    user_results = []
    if request.method == 'GET':
        query = request.GET['q']
        results = SearchQuerySet().using('default').filter(text=query)
        if len(results) == 1:
            return redirect(results[0].object)
        else:
            for nr in results:
                user_results.append(nr.object.user)
    return render(request, 'search.html', {'user_results': user_results})