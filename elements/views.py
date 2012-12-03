from django.shortcuts import render
from elements.forms import ElementCreateForm, ElementEditForm
from elements.models import Element
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from middleware.http import Http403
from django.shortcuts import redirect

@login_required
def create (request):
    if request.method == "POST":
        form = ElementCreateForm(request.POST, instance=Element(owner=request.user))
        if form.is_valid():
            return redirect(form.save())
    else:
        form = ElementCreateForm(instance=Element(owner=request.user))
    return render(request, 'elements/create.html', {'form': form})

@login_required
def list (request):
    elements = Element.objects.filter(owner=request.user)
    return render(request, 'elements/list.html', {'elements': elements})

def view (request, element_id):
    element = get_object_or_404(Element, id=element_id)
    return render(request, 'elements/view.html', {'element': element})

@login_required
def edit (request, element_id):
    element = get_object_or_404(Element, id=element_id)
    if element.owner != request.user:
        raise Http403
    if request.method == "POST":
        form = ElementEditForm(request.POST, instance=element)
        if form.is_valid():
            element = form.save(commit=False)
            element.save()
            return redirect(element)
    else:
        form = ElementEditForm(instance=element)
    return render(request, 'elements/edit.html', {'element': element,
                                                  'form': form})