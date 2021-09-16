from django.shortcuts import render
from django.views.generic import edit
from django.views import generic

from .models import Entry, Feeling, Place
from .forms import PlaceForm, FeelingForm, EntryForm
# def dashboard(request):    
#     return render(request, 'wru/base.html', context={})



# @method_decorator(login_required(login_url='/login/'), name='dispatch')
class PlaceCreateView(edit.CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'wru/place/create.html'


class PlaceDetailView(generic.DeleteView):
    model = Place
    context_object_name = 'place'
    template_name = 'wru/place/details.html'


class PlaceUpdateView(edit.UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'wru/place/update.html'


class PlaceDeleteView(edit.DeleteView):
    model = Place
    template_name = 'wru/generic/delete-prompt.html'
    success_url ="/"


class FeelingCreateView(edit.CreateView):
    model = Feeling
    form_class = FeelingForm
    template_name = 'wru/feeling/create.html'


class FeelingDetailView(generic.DeleteView):
    model = Feeling
    context_object_name = 'feeling'
    template_name = 'wru/feeling/details.html'


class FeelingUpdateView(edit.UpdateView):
    model = Feeling
    form_class = FeelingForm
    template_name = 'wru/feeling/update.html'


class FeelingDeleteView(edit.DeleteView):
    model = Feeling
    template_name = 'wru/generic/delete-prompt.html'
    success_url ="/"


class EntryCreateView(edit.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'wru/entry/create.html'


class EntryDetailView(generic.DeleteView):
    model = Entry
    context_object_name = 'entry'
    template_name = 'wru/entry/details.html'


class EntryUpdateView(edit.UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'wru/entry/update.html'


class EntryDeleteView(edit.DeleteView):
    model = Entry
    template_name = 'wru/generic/delete-prompt.html'
    success_url ="/"


class EntryListView(generic.ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'wru/entry/list.html'    