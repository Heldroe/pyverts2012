from django.shortcuts import render
from actstream.models import actor_stream, user_stream

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from haystack.query import SearchQuerySet

from elements.models import Photo

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home (request):
    if request.user.is_authenticated():
        u_stream = user_stream(request.user)
        return render(request, 'user_home.html', {'home': True, 'user_stream': u_stream})
    else:
        return render(request, 'home.html', {'home': True})

def discover (request):
    return render(request, 'discover.html')

@csrf_exempt
def search (request):
    tab_e_results = []
    tab_u_results = []
    query = ""
    if request.method == 'GET':
        query = request.GET['q']
        e_results = SearchQuerySet().filter(element=query)
        u_results = SearchQuerySet().filter(profile=query)
        if len(e_results) == 1 and len(u_results) == 0:
            return redirect(e_results[0].object)
        elif len(u_results) == 1 and len(e_results) == 0:
            return redirect(u_results[0].object)
        paginator = Paginator(e_results, 5)
        more = paginator.num_pages > 1
        for nr in paginator.page(1).object_list:
            try:
                main_pic = Photo.objects.get(element=nr.object, main=True)
                nr.object.main_pic = main_pic
            except Photo.DoesNotExist:
                pass
            tab_e_results.append(nr.object)
        for nr in u_results:
            tab_u_results.append(nr.object.user)
    return render(request, 'search.html', {'user_results': tab_u_results, 'element_results': tab_e_results, 'more': more, 'query':query, 'total':paginator.count})

def search_more (request, page_id=1):
    tab_e_results = []
    next = False
    previous = True
    next_n = page_id
    previous_n = page_id
    if request.method == 'GET':
        query = request.GET['q']
        e_results = SearchQuerySet().filter(element=query)
        if len(e_results) == 1 and len(u_results) == 0:
            return redirect(e_results[0].object)
        paginator = Paginator(e_results, 20)
        p = paginator.page(page_id)
        next = p.has_next()
        next_n = int(page_id) + 1
        previous = p.has_previous()
        previous_n = int(page_id) - 1
        for nr in p.object_list:
            try:
                main_pic = Photo.objects.get(element=nr.object, main=True)
                nr.object.main_pic = main_pic
            except Photo.DoesNotExist:
                pass
            tab_e_results.append(nr.object)
    return render(request, 'search_more.html', {'element_results': tab_e_results, 'next': next, 'previous': previous, 'next_n': next_n, 'previous_n': previous_n})

def theme (request, new_theme):
    try:
        print request.session["theme"]
    except KeyError:
        print "MERDE"
    if (new_theme == 'canada'):
        request.session["theme"] = "content_ac.html"
    else:
        request.session["theme"] = "content.html"
    return redirect(reverse('pyverts2012.views.home'))