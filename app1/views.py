from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from app1.forms import ItemForm
from app1.models import Item


# Create your views here.

def list_item(request):
    items = Item.objects.order_by('-timestamp')
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'home.html', context)


def search(request):
    items = Item.objects.order_by('-timestamp')
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    # search
    qs = Item.objects.all()
    query = request.GET.get('q')
    if query:
        qs = qs.filter(
            Q(food_title__icontains=query) |
            Q(food_type__icontains=query) |
            Q(valid_from__icontains=query) |
            Q(valid_to__icontains=query)
        ).distinct()
        if query and qs:
            messages.success(request, "Search Item found '%s' ...!!!" % (query))
        else:
            messages.warning(request, "Search Item Not found '%s' ...!!!" % (query),
                             "search another Item...???")
    context = {
        "item_obj": qs,
        'items': items,
        'form': form,
    }
    return render(request, 'search_results.html', context)
