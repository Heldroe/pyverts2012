from django.shortcuts import render
from actstream.models import actor_stream, user_stream

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from haystack.query import SearchQuerySet

from elements.models import Photo

def home (request):
    if request.user.is_authenticated():
        u_stream = user_stream(request.user)
        return render(request, 'user_home.html', {'home': True, 'user_stream': u_stream})
    else:
        return render(request, 'home.html', {'home': True})

@csrf_exempt
def search (request):
    tab_e_results = []
    tab_u_results = []
    if request.method == 'GET':
        query = request.GET['q']
        e_results = SearchQuerySet().filter(element=query)
        print e_results
        u_results = SearchQuerySet().filter(profile=query)
        print u_results
        if len(e_results) == 1 and len(u_results) == 0:
            return redirect(e_results[0].object)
        elif len(u_results) == 1 and len(e_results) == 0:
            return redirect(u_results[0].object)
        for nr in e_results:
            try:
                main_pic = Photo.objects.get(element=nr.object, main=True)
                nr.object.main_pic = main_pic
            except Photo.DoesNotExist:
                pass
            tab_e_results.append(nr.object)
        for nr in u_results:
            tab_u_results.append(nr.object.user)
    return render(request, 'search.html', {'user_results': tab_u_results, 'element_results': tab_e_results})