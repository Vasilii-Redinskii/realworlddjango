from django.contrib import admin
from . import models
from utils.models import places_left, MORE50, LESS50, SOLD_AUT


class ReviewInline(admin.TabularInline):
    model = models.Review
    readonly_fields = ('id', 'user', 'rate', 'text', 'created', 'updated')
    can_delete = False

class FillEventFilter(admin.SimpleListFilter):
    title = 'Заполненость'
    parameter_name = 'fill_event_filter'

    def lookups(self, request, model_admin):
        filter_list = (
            ('MORE50', MORE50),
            ('LESS50', LESS50),
            ('SOLD_AUT', SOLD_AUT)
        )
        return filter_list

    def queryset(self, request, queryset):
        filter_value = self.value()

        return queryset.filter()


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_start', 'participants_number', 'is_private', 'category', 'display_enroll_count', 'display_places_left' ]
    list_filter = ['category', 'features', FillEventFilter]
    search_fields = ['title', ]
    ordering = ['date_start', ]
    readonly_fields = ['display_enroll_count', 'display_places_left', ]
    inlines = [ReviewInline]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_event_count', ]
    list_display_links = ['id', 'title', ]


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]


@admin.register(models.Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', ]
    list_display_links = ['id', 'user', 'event', ]
    list_select_related = ['user', ]

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', ]
    list_display_links = ['id', 'user', 'event', ]
    list_filter = ['created', 'event', ]
    readonly_fields = ['created', 'updated', 'id', ]
