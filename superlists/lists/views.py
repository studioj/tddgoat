# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    new_item = request.POST['item_text']
    Item.objects.create(text=new_item)
    return redirect('/lists/the-only-list-in-the-world/')
