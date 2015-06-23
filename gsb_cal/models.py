# coding: utf-8
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(editable=False, default=False, verbose_name='Silindi')
    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=64, verbose_name = u'adı',unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Ülkeler"
        verbose_name = "Ülke"
        ordering = ['name']

    def __unicode__(self):
        return "%s" % (self.name)

class City(BaseModel):
    country = models.ForeignKey(Country, default = 0)
    name = models.CharField(max_length=64, verbose_name = u'adı',unique=True)
    order_number = models.IntegerField(default=10)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Şehirler"
        verbose_name = "Şehir"
        ordering = ['order_number','name']

    def __unicode__(self):
        return "%s" % (self.name)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField()
    def __unicode__(self):              # __str__ on Python 3
        return "%s %s" %(self.first_name,self.last_name)

class Dj(models.Model):
    stage_name = models.CharField(max_length=30,unique=True)
    slug = models.SlugField()
    def __unicode__(self):              # __str__ on Python 3
        return "%s" % (self.stage_name)

class DanceType(models.Model):
    name = models.CharField(max_length=30,unique=True)
    slug = models.SlugField()
    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Band(BaseModel):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField()
    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Musician(Person):
    instrument = models.CharField(max_length=100,blank=True)

class Event(BaseModel):
    event_name = models.CharField(max_length=100,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    slogan = models.CharField(max_length=100,blank=True)
    EVENT_TYPE_CHOICES = (
        ('Ws', 'Workshop'),
        ('Ex', 'Exchange'),
        ('Dc', 'Dance Camp'),
        ('Co', 'Concert'),
        ('We', 'Weekend'),
    )
    event_type = models.CharField(max_length=2,choices=EVENT_TYPE_CHOICES,default="Ws")
    city = models.ForeignKey(City)
    website = models.URLField(null=True,blank=True)
    fb_page = models.URLField(null=True,blank=True)
    fb_event = models.URLField(null=True,blank=True)
    slug = models.SlugField()
    dance_type = models.ManyToManyField(DanceType,blank=True)
    teachers = models.ManyToManyField(Person,blank=True,related_name=u"teachers")
    bands = models.ManyToManyField(Band,blank=True)
    djs = models.ManyToManyField(Dj,blank=True,related_name=u"djs")
    def __unicode__(self):              # __str__ on Python 3
        return self.event_name
    def past_event(self):
        return self.end_date <= timezone.now().date() - datetime.timedelta(days=1)
    past_event.admin_order_field = 'end_date'
    past_event.boolean = True
    past_event.short_description = 'coming event?'

    class Meta:
        ordering = ["-start_date"]

"""
    def get_as_json(self):
        from django.template.loader import render_to_string
        from django.core.cache import cache
        key = 'get_as_json_' + str(self.id)
        response = cache.get(key)
        timeout = 60 * 60 * 6
        if response:
            return response
        else:
            response = render_to_string('index.html', { 'project': self,})
            cache.set(key, response, timeout)
            return response
"""
