from django.contrib import admin
from .models import Tour, TourProgramm, Place, Tariff
# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = [
        'city', 'slug', 'region', 'country'
    ]
    prepopulated_fields = {'slug': ('city', 'region')}


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    fields = [
        'title', 'slug', 'conditions', 'price'
    ]

    list_display = [
        'title', 'price'
    ]

    prepopulated_fields = {'slug': ('title', )}

    list_editable = [
        'price'
    ]


@admin.register(TourProgramm)
class TourProgrammAdmin(admin.ModelAdmin):
    fields = [
        'title', 'tour', 'order', 'description', 'photo',
    ]

    list_display = [
        'title', 'tour'
    ]

    search_fields = [
        'title', 'tour'
    ]


class TourProgrammInLine(admin.StackedInline):
    model = TourProgramm


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fields = [
        'title', 'slug', 'description', 'tariff', 'place', 'start_date', 'end_date', 'is_active', 'photo'
    ]
    list_display = [
        'title', 'place', 'created'
    ]

    search_fields = [
        'title', 'place'
    ]
    save_on_top = True

    prepopulated_fields = {'slug': ('title', )}
    inlines = [TourProgrammInLine]
