from django.urls import path

from . import views


app_name = 'wru'

urlpatterns = [
    path('', views.EntryListView.as_view(), name='home'),
    path('place', views.PlaceListView.as_view(), name='place-list'),
    path('place/create', views.PlaceCreateView.as_view(), name='place-create'),
    path('place/<int:pk>', views.PlaceDetailView.as_view(), name='place-details'),
    path('place/<int:pk>/update', views.PlaceUpdateView.as_view(), name='place-update'),
    path('place/<int:pk>/delete', views.PlaceDeleteView.as_view(), name='place-delete'),
    path('place/<int:place_pk>/entries', views.EntryListViewByPlace.as_view(), name='place-entries'),

    path('feeling', views.FeelingListView.as_view(), name='feeling-list'),
    path('feeling/create', views.FeelingCreateView.as_view(), name='feeling-create'),
    path('feeling/<int:pk>', views.FeelingDetailView.as_view(), name='feeling-details'),
    path('feeling/<int:pk>/update', views.FeelingUpdateView.as_view(), name='feeling-update'),
    path('feeling/<int:pk>/delete', views.FeelingDeleteView.as_view(), name='feeling-delete'),
    path('feeling/<int:feeling_pk>/entries', views.EntryListViewByFeeling.as_view(), name='feeling-entries'),

    path('entry', views.EntryListView.as_view(), name='entry-list'),
    path('entry/create', views.EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>', views.EntryDetailView.as_view(), name='entry-details'),
    path('entry/<int:pk>/update', views.EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete', views.EntryDeleteView.as_view(), name='entry-delete'),
    
]