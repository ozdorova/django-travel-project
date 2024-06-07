from django.contrib import admin

from .models import Place, Programm, Tariff, Tour


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = [
        'city',
        'region',
        'country'
    ]


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'conditions',
        'price'
    ]

    list_display = [
        'title',
        'price'
    ]

    list_editable = [
        'price'
    ]


@admin.register(Programm)
class TourProgrammAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'tour',
        'order',
        'description',
        'photo',
    ]

    list_display = [
        'title',
        'tour'
    ]

    search_fields = [
        'title',
        'tour'
    ]


class TourProgrammInLine(admin.StackedInline):
    model = Programm


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fields = [
        'owner',
        'title',
        'description',
        'tariffs',
        'places',
        'start_date',
        'end_date',
        'is_active',
        'photo',
    ]
    list_display = [
        'title',
        'is_active',
        'created',
    ]

    search_fields = [
        'title',
    ]
    list_editable = [
        'is_active'
    ]
    save_on_top = True

    inlines = [TourProgrammInLine]
