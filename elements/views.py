from django.shortcuts import render
from elements.forms import ElementCreateForm, ElementEditForm, PhotoAddForm
from elements.models import Element, Photo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from middleware.http import Http403
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

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
    main_pic = False
    cover_pic = False
    photos = Photo.objects.filter(element=element)
    try:
        main_pic = Photo.objects.get(element=element, main=True)
    except Photo.DoesNotExist:
        pass
    try:
        cover_pic = Photo.objects.get(element=element, cover=True)
    except Photo.DoesNotExist:
        pass
    return render(request, 'elements/view.html', {'element': element,
                                                  'photos': photos,
                                                  'main_photo': main_pic,
                                                  'cover_photo': cover_pic})

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
    photos = Photo.objects.filter(element=element)
    return render(request, 'elements/edit.html', {'element': element,
                                                  'form': form,
                                                  'photos': photos})

@login_required
def edit_photos (request, element_id):
    element = get_object_or_404(Element, id=element_id)
    if element.owner != request.user:
        raise Http403
    photos = Photo.objects.filter(element=element)
    return render(request, 'elements/edit_photos.html', {'element': element, 'photos': photos})

@login_required
def add_photo (request, element_id):
    element = get_object_or_404(Element, id=element_id)
    if element.owner != request.user:
        raise Http403
    if request.method == "POST":
        form = PhotoAddForm(request.POST, request.FILES, instance=Photo(element=element))
        if form.is_valid():
            form.save()
            return redirect(reverse('elements.views.edit', args=[str(element.id)]))
    else:
        form = PhotoAddForm(instance=Photo(element=element))
    return render(request, 'elements/add_photo.html', {'element': element, 'form': form})

@login_required
def main_photo (request, element_id, photo_id):
    element = get_object_or_404(Element, id=element_id)
    photo = get_object_or_404(Photo, id=photo_id)
    if element.owner != request.user or photo.element != element:
        raise Http403
    try:
        old_main = Photo.objects.get(element=element, main=True)
        old_main.main = False
        old_main.save()
    except Photo.DoesNotExist:
        pass
    photo.main = True
    photo.save()
    return redirect(reverse('elements.views.edit', args=[str(element.id)]))

@login_required
def cover_photo (request, element_id, photo_id):
    element = get_object_or_404(Element, id=element_id)
    photo = get_object_or_404(Photo, id=photo_id)
    if element.owner != request.user or photo.element != element:
        raise Http403
    try:
        old_cover = Photo.objects.get(element=element, cover=True)
        old_cover.cover = False
        old_cover.save()
    except Photo.DoesNotExist:
        pass
    photo.cover = True
    photo.save()
    return redirect(reverse('elements.views.edit', args=[str(element.id)]))

@login_required
def delete_photo (request, element_id, photo_id):
    element = get_object_or_404(Element, id=element_id)
    photo = get_object_or_404(Photo, id=photo_id)
    if element.owner != request.user or photo.element != element:
        raise Http403
    photo.delete()
    return redirect(reverse('elements.views.edit', args=[str(element.id)]))