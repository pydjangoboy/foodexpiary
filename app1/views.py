from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from app1.forms import ItemForm
from app1.models import Item


# Create your views here.
@login_required
def list_item(request):
    items = Item.objects.order_by('-timestamp')
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Item added...!!!")
            return redirect('item_list')
    else:
        form = ItemForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'home.html', context)


# update view for details
@login_required
def item_update(request, pk):
    context = {}
    obj = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully updated item ...!!!")
        return redirect('item_list')
    context["form"] = form
    return render(request, "update_item.html", context)


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Successfully deleted item ...!!!")
        return redirect('item_list')
    return render(request, 'delete_item.html', {'object': item})


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
