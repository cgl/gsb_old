# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model("yourappname", "Person")
    for person in Person.objects.all():
        person.name = "%s %s" % (person.first_name, person.last_name)
        person.save()

def insert_person(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.

    Person = apps.get_model("gsb_cal", "Person")
    for person in PERSON_OBJS:
        per = person['fields']
        person_obj = Person.objects.create(first_name = per['first_name'], last_name = per['last_name'], slug = per['slug'])
        person_obj.save()


def insert_dances(apps, schema_editor):
    DanceType = apps.get_model("gsb_cal", "DanceType")
    for obj_ser in DANCES_OBJS:
        obj_dict = obj_ser['fields']
        obj = DanceType.objects.create(name = obj_dict['name'], slug = obj_dict['slug'])
        obj.save()

def insert_bands(apps, schema_editor):
    Band = apps.get_model("gsb_cal", "Band")
    for obj_ser in BANDS_OBJS:
        obj_dict = obj_ser['fields']
        obj = Band.objects.create(name = obj_dict['name'], slug = obj_dict['slug'])
        obj.save()

def insert_events(apps, schema_editor):
    Event = apps.get_model("gsb_cal", "Event")
    d_format = '%Y-%m-%d'
    for obj_ser in EVENT_OBJS:
        obj_dict = obj_ser['fields']
        obj = Event.objects.create(start_date=datetime.datetime.strptime(obj_dict['start_date'], d_format).date(),
                                   event_name = obj_dict['event_name'],
                                   end_date=datetime.datetime.strptime(obj_dict['end_date'], d_format).date(),
                                   slogan=obj_dict['slogan'], event_type=obj_dict['event_type'],
                                   city_id=obj_dict['city'],
                                   website=obj_dict['website'],
                                   slug = obj_dict['slug'])
        obj.save()


PERSON_OBJS = [#{"fields": {"first_name": "Ahter", "last_name": u"Sonmez", "slug": "ahter-sonmez"}, "model": "gsb_cal.person", "pk": 1},
{"fields": {"first_name": "Kevin St.", "last_name": "Laurent", "slug": "kevin-st-laurent"}, "model": "gsb_cal.person", "pk": 2},
{"fields": {"first_name": "Pontus", "last_name": "Persson", "slug": "pontus-persson"}, "model": "gsb_cal.person", "pk": 3},
{"fields": {"first_name": "Rikard", "last_name": "Ekstrand", "slug": "rikard-ekstrand"}, "model": "gsb_cal.person", "pk": 4},
{"fields": {"first_name": "Daniel", "last_name": "Heedman", "slug": "daniel-heedman"}, "model": "gsb_cal.person", "pk": 5},
{"fields": {"first_name": "Frida", "last_name": "Segerdahl", "slug": "frida-segerdahl"}, "model": "gsb_cal.person", "pk": 6},
{"fields": {"first_name": "Lennart", "last_name": "Westerlund", "slug": "lennart-westerlund"}, "model": "gsb_cal.person", "pk": 7},
{"fields": {"first_name": "Nick", "last_name": "Williams", "slug": "nick-williams"}, "model": "gsb_cal.person", "pk": 8},
{"fields": {"first_name": "Peter", "last_name": "Loggins", "slug": "peter-loggins"}, "model": "gsb_cal.person", "pk": 9},
{"fields": {"first_name": "Ramona", "last_name": "Staffeld", "slug": "ramona-staffeld"}, "model": "gsb_cal.person", "pk": 10},
{"fields": {"first_name": "Remy", "last_name": "Kouakou", "slug": "remy-kouakou"}, "model": "gsb_cal.person", "pk": 11},
{"fields": {"first_name": "Sylvia", "last_name": "Sykes", "slug": "sylvia-sykes"}, "model": "gsb_cal.person", "pk": 12},
{"fields": {"first_name": "Tony", "last_name": "Jackson", "slug": "tony-jackson"}, "model": "gsb_cal.person", "pk": 13},
{"fields": {"first_name": "Chazz", "last_name": "Young", "slug": "chazz-young"}, "model": "gsb_cal.person", "pk": 14},
{"fields": {"first_name": "Hanna", "last_name": "Lundmark", "slug": "hanna-lundmark"}, "model": "gsb_cal.person", "pk": 15},
{"fields": {"first_name": "Jo", "last_name": "Hoffberg", "slug": "jo-hoffberg"}, "model": "gsb_cal.person", "pk": 16},
{"fields": {"first_name": "Mattias", "last_name": "Lundmark", "slug": "mattias-lundmark"}, "model": "gsb_cal.person", "pk": 17},
{"fields": {"first_name": "Katja", "last_name": "Hrastar", "slug": "katja-hrastar"}, "model": "gsb_cal.person", "pk": 18},
{"fields": {"first_name": "Marie", "last_name": "N'diaye", "slug": "marie-ndiaye"}, "model": "gsb_cal.person", "pk": 19},
{"fields": {"first_name": "Mikey", "last_name": "Pedroza", "slug": "mikey-pedroza"}, "model": "gsb_cal.person", "pk": 20},
{"fields": {"first_name": "Skye", "last_name": "Humphries", "slug": "skye-humphries"}, "model": "gsb_cal.person", "pk": 21},
{"fields": {"first_name": "Chester", "last_name": "Whitmore", "slug": "chester-whitmore"}, "model": "gsb_cal.person", "pk": 22},
{"fields": {"first_name": "Gast\u00f3n", "last_name": "Fern\u00e1ndez", "slug": "gaston-fernandez"}, "model": "gsb_cal.person", "pk": 23},
{"fields": {"first_name": "Henric", "last_name": "Stillman", "slug": "henric-stillman"}, "model": "gsb_cal.person", "pk": 24},
{"fields": {"first_name": "Juan", "last_name": "Villafa\u00f1e", "slug": "juan-villafane"}, "model": "gsb_cal.person", "pk": 25},
{"fields": {"first_name": "Mikaela", "last_name": "Hellsten", "slug": "mikaela-hellsten"}, "model": "gsb_cal.person", "pk": 26},
{"fields": {"first_name": "Naomi", "last_name": "Uyama", "slug": "naomi-uyama"}, "model": "gsb_cal.person", "pk": 27},
{"fields": {"first_name": "Nicolas", "last_name": "Deniau", "slug": "nicolas-deniau"}, "model": "gsb_cal.person", "pk": 28},
{"fields": {"first_name": "Peter", "last_name": "Strom", "slug": "peter-strom"}, "model": "gsb_cal.person", "pk": 29},
{"fields": {"first_name": "Sharon", "last_name": "Davis", "slug": "sharon-davis"}, "model": "gsb_cal.person", "pk": 30},
{"fields": {"first_name": "Dawn", "last_name": "Hampton", "slug": "dawn-hampton"}, "model": "gsb_cal.person", "pk": 31},
{"fields": {"first_name": "Fredrik", "last_name": "Dahlberg", "slug": "fredrik-dahlberg"}, "model": "gsb_cal.person", "pk": 32},
{"fields": {"first_name": "Sandra", "last_name": "Klack", "slug": "sandra-klack"}, "model": "gsb_cal.person", "pk": 33},
{"fields": {"first_name": "JB", "last_name": "Mino", "slug": "jb-mino"}, "model": "gsb_cal.person", "pk": 34}]

DANCES_OBJS = [{"fields": {"name": "Lindy Hop", "slug": "lindy-hop"}, "model": "gsb_cal.dancetype", "pk": 1},
{"fields": {"name": "Balboa", "slug": "balboa"}, "model": "gsb_cal.dancetype", "pk": 2},
{"fields": {"name": "Blues", "slug": "blues"}, "model": "gsb_cal.dancetype", "pk": 3},
{"fields": {"name": "Charleston", "slug": "charleston"}, "model": "gsb_cal.dancetype", "pk": 4},]

BANDS_OBJS = [{"fields": {"modified_date": "2015-06-06T23:54:08.463Z", "slug": "hot-sugar-band", "create_date": "2015-06-06T23:54:08.463Z", "is_deleted": False, "name": "Hot Sugar Band"}, "model": "gsb_cal.band", "pk": 1},
{"fields": {"modified_date": "2015-06-06T23:59:16.141Z", "slug": "gordon-webster-band", "create_date": "2015-06-06T23:59:16.141Z", "is_deleted": False, "name": "Gordon Webster Band"}, "model": "gsb_cal.band", "pk": 2},
{"fields": {"modified_date": "2015-06-07T00:00:04.820Z", "slug": "carling-family", "create_date": "2015-06-07T00:00:04.820Z", "is_deleted": False, "name": "Carling Family"}, "model": "gsb_cal.band", "pk": 3},
{"fields": {"modified_date": "2015-06-07T00:26:34.468Z", "slug": "gentlemen-and-gangsters", "create_date": "2015-06-07T00:26:34.468Z", "is_deleted": False, "name": "Gentlemen & Gangsters"}, "model": "gsb_cal.band", "pk": 4},]

EVENT_OBJS = [{"fields": {"website": "", "modified_date": "2015-06-07T00:14:05.033Z", "create_date": "2015-06-07T00:13:45.799Z", "event_type": "Dc", "end_date": "2015-06-07", "city": 2, "event_name": "Herrang Dance Camp", "slogan": "The Classic", "dance_type": [1, 2, 3, 4], "slug": "herring-dance-camp", "teachers": [1], "bands": [1, 2, 3], "is_deleted": False, "start_date": "2015-06-07"}, "model": "gsb_cal.event", "pk": 2}, {"fields": {"website": "", "modified_date": "2015-06-07T00:27:37.374Z", "create_date": "2015-06-07T00:26:50.774Z", "event_type": "Ws", "end_date": "2015-06-07", "city": 3, "event_name": "The Mooche", "slogan": "Distilled", "dance_type": [1, 2, 3], "slug": "the-mooche", "teachers": [1, 2], "bands": [1], "is_deleted": False, "start_date": "2015-06-07"}, "model": "gsb_cal.event", "pk": 3}, {"fields": {"website": "", "modified_date": "2015-06-07T00:28:51.308Z", "create_date": "2015-06-07T00:28:51.308Z", "event_type": "Ws", "end_date": "2015-06-07", "city": 2, "event_name": "The Snowball", "slogan": "The best", "dance_type": [], "slug": "the-snowball", "teachers": [], "bands": [3], "is_deleted": False, "start_date": "2015-06-07"}, "model": "gsb_cal.event", "pk": 4}, {"fields": {"website": "http://www.crossoveristanbul.com", "modified_date": "2015-06-07T00:56:03.456Z", "create_date": "2015-06-07T00:30:03.096Z", "event_type": "Ws", "end_date": "2015-06-07", "city": 1, "event_name": "Crossover Istanbul", "slogan": "Hop Over \u0130\u015fte", "dance_type": [1, 3], "slug": "crossover-istanbul", "teachers": [], "bands": [], "is_deleted": False, "start_date": "2015-06-07"}, "model": "gsb_cal.event", "pk": 5}, {"fields": {"website": "", "modified_date": "2015-06-07T00:52:59.031Z", "create_date": "2015-06-07T00:31:44.114Z", "event_type": "Ws", "end_date": "2015-06-07", "city": 3, "event_name": "Cork Jazz Dance Exchange", "slogan": "", "dance_type": [1, 2, 3, 4], "slug": "cork-jazz-dance-exchange", "teachers": [1], "bands": [], "is_deleted": False, "start_date": "2015-06-07"}, "model": "gsb_cal.event", "pk": 6}, {"fields": {"website": "", "modified_date": "2015-06-07T01:34:11.389Z", "create_date": "2015-06-07T00:57:14.787Z", "event_type": "Ws", "end_date": "2015-06-17", "city": 4, "event_name": "Lindy Shock", "slogan": "a big shock", "dance_type": [1], "slug": "lindy-shock", "teachers": [1, 15, 17, 29], "bands": [2], "is_deleted": False, "start_date": "2015-06-17"}, "model": "gsb_cal.event", "pk": 7}]


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(insert_person),
        migrations.RunPython(insert_dances),
        migrations.RunPython(insert_bands),
        migrations.RunPython(insert_events),
    ]
