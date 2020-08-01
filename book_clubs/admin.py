from django.contrib import admin
from . import models
from django.utils.html import mark_safe


@admin.register(models.Category_BookReview)
class CategoryAdmin(admin.ModelAdmin):
    """ Category_BookReview Admin Definition """

    list_display = (
        "name",
        "id",
    )


@admin.register(models.BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    """ BookReview Admin Definition """

    list_display = (
        "title",
        "sub_title",
        "category_BookReview",
        "created",
        "updated",
        "id",
    )

    list_filter = ("category_BookReview",)

    search_fields = ("title",)
