from django.contrib import admin
from . import models
from utils.models import places_left, MORE50, LESS50, SOLD_AUT


class ReviewInline(admin.TabularInline):
    model = models.Review
    extra = 0
    readonly_fields = ('id', 'user', 'rate', 'text', 'created', 'updated')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class FillEventFilter(admin.SimpleListFilter):
    title = 'Заполненость'
    parameter_name = 'fill_event_filter'

    def lookups(self, request, model_admin):
        filter_list = (
            (MORE50, MORE50),
            (LESS50, LESS50),
            (SOLD_AUT, SOLD_AUT)
        )
        return filter_list

    def queryset(self, request, queryset):
        filter_value = self.value()
        list_id = []
        if filter_value == None:
            return queryset

        for value in queryset:
            if filter_value in value.display_places_left():
                list_id.append(value.id)
        return queryset.filter(id__in=list_id)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_start', 'participants_number', 'is_private', 'category',
                    'display_enroll_count', 'display_places_left', 'rate', 'logo_url']
    list_filter = [FillEventFilter, 'category', 'features', ]
    search_fields = ['title', ]
    ordering = ['date_start', ]
    readonly_fields = ['display_enroll_count', 'display_places_left', ]
    inlines = [ReviewInline]
    filter_horizontal = ('features', )

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
