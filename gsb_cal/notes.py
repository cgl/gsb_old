from gsb_cal import models

turkey = models.Country.objects.create(name="turkey",)
ist = models.City.objects.create(name="istanbul",country=turkey)
sweden = models.Country.objects.create(name="sweden",)
stockholm = models.City.objects.create(name="stockholm",country=sweden)
ireland = models.Country.objects.create(name="ireland",)
cork = models.City.objects.create(name="cork",country=ireland)
hungary = models.Country.objects.create(name="hungary",)
budapest = models.City.objects.create(name="budapest",country=hungary)
