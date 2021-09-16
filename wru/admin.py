# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Place, Feeling, Entry


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at', 'name')
    list_filter = ('created_at', 'modified_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Feeling)
class FeelingAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at', 'name', 'icon')
    list_filter = ('created_at', 'modified_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'modified_at',
        'place',
        'date',
        'why',
        'feeling',
        'tags',
    )
    list_filter = ('created_at', 'modified_at', 'place', 'date', 'feeling', 'tags')
    date_hierarchy = 'created_at'