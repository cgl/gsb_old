from django.contrib import admin

from django.contrib import admin
from models import Event,City, Country, DanceType ,Band, Musician ,Person,Dj

class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name','city','start_date','past_event']
    list_filter = ('start_date','city',)
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
    filter_horizontal = ('dance_type','teachers','bands','djs')
    prepopulated_fields = {"slug": ("event_name",)}
    search_fields = ['event_name']
    fieldsets = (
        (None, {
            'fields': ('event_name', 'slogan', 'start_date', 'end_date','event_type','city','website','slug')
        }),
        ('Advanced options', {
            #'classes': ('collapse',),
            'fields': ('dance_type', 'teachers', 'bands','djs')
        }),
    )

class CityAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('name', 'order_number')
    search_fields = ('name',)
    list_editable = ('order_number',)
    #ordering = ('province_id',)
    prepopulated_fields = {"slug": ("name",)}

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class DanceTypeAdmin(admin.ModelAdmin):
    list_display= ['name']
    prepopulated_fields = {"slug": ("name",)}

class BandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class MusicianAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name",)}

class DjAdmin(admin.ModelAdmin):
    pass
#    prepopulated_fields = {"slug": ("name",)}

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name",)}

#admin.site.register(, )
admin.site.register(Dj,DjAdmin )
admin.site.register(Person, PersonAdmin )
admin.site.register(Band, BandAdmin)
#admin.site.register(Musician,MusicianAdmin)
admin.site.register(DanceType, DanceTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
