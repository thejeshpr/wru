from django.db import models
from django.db.models.base import Model
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager


class Place(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=300, unique=True)
    url = models.URLField(max_length=3000, blank=True, null=True)

    def get_absolute_url(self):        
        return reverse('wru:place-details', kwargs=dict(pk=self.pk))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Place, self).save(*args, **kwargs)


class Feeling(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, unique=True)
    icon = models.CharField(max_length=100, unique=True, default='<i class="las la-question-circle"></i>')

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def get_absolute_url(self):        
        return reverse('wru:feeling-details', kwargs=dict(pk=self.pk))

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if self.icon.startswith("<i class="):
            self.icon = self.icon.split('"')[1]
        return super(Feeling, self).save(*args, **kwargs)


class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    place = models.ForeignKey('Place', related_name='entries', on_delete=models.CASCADE)    
    date = models.DateField(auto_now=False, auto_now_add=False)
    why = models.CharField(help_text="Why at this Place?", max_length=500, blank=True, null=True)
    feeling = models.ForeignKey('Feeling', related_name='entries', on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self) -> str:
        # return f"{self.place.name}:{self.date}"
        return self.why

    def __repr__(self) -> str:
        # return f"{self.place.name}:{self.date}"
        return self.why

    def get_absolute_url(self):        
        return reverse('wru:entry-details', kwargs=dict(pk=self.pk))
        