from django.contrib import admin

# Register your models here.
from models import Advertisement, AdvertisementStatusChoices


admin.site.register(Advertisement)

admin.site.register(AdvertisementStatusChoices)


