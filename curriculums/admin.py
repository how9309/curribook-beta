from django.contrib import admin
from . import models
from django.utils.html import mark_safe


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category Admin Definition """

    list_display = (
        "name",
        "id",
    )


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    """ Curriculum Admin Definition """

    inlines = (PhotoInline,)

    list_display = (
        "title",
        "sub_title",
        "category",
        "recommendation",
        "popular",
        "new",
        "today",
        "created",
        "updated",
        "id",
    )

    list_filter = ("category",)

    search_fields = ("title",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
