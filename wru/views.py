from django.db import models
from django.shortcuts import render
from django.views.generic import edit
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Entry, Feeling, Place
from .forms import PlaceForm, FeelingForm, EntryForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlaceCreateView(edit.CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'wru/place/create.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlaceDetailView(generic.DeleteView):
    model = Place
    context_object_name = 'place'
    template_name = 'wru/place/details.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlaceUpdateView(edit.UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'wru/place/update.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlaceDeleteView(edit.DeleteView):
    model = Place
    template_name = 'wru/generic/delete-prompt.html'
    success_url ="/"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlaceListView(generic.ListView):
    model = Place
    template_name = "wru/place/list.html"
    context_object_name = "places"    


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeelingCreateView(edit.CreateView):
    model = Feeling
    form_class = FeelingForm
    template_name = 'wru/feeling/create.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeelingDetailView(generic.DeleteView):
    model = Feeling
    context_object_name = 'feeling'
    template_name = 'wru/feeling/details.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeelingUpdateView(edit.UpdateView):
    model = Feeling
    form_class = FeelingForm
    template_name = 'wru/feeling/update.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeelingDeleteView(edit.DeleteView):
    model = Feeling
    template_name = 'wru/generic/delete-prompt.html'
    success_url ="/"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FeelingListView(generic.ListView):
    model = Feeling
    template_name = "wru/feeling/list.html"
    context_object_name = "feelings"    


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EntryCreateView(edit.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'wru/entry/create.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EntryDetailView(generic.DeleteView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'wru/entry/details.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EntryUpdateView(edit.UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'wru/entry/update.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EntryDeleteView(edit.DeleteView):
    model = Entry
    template_name = 'wru/generic/delete-prompt.html'
    success_url ="/"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EntryListView(generic.ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'wru/entry/list.html'

    def get_queryset(self):
        return Entry.objects.order_by('-date')