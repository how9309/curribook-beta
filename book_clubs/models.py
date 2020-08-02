from django.db import models
from core import models as core_models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField


class AbstractItem_BookReview(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category_BookReview(AbstractItem_BookReview):
    class Meta:
        verbose_name_plural = "Categories_BookReview"
        ordering = ["name"]


class BookReview(core_models.TimeStampedModel):
    """ BookReview Model Definition """

    author = models.ForeignKey("users.User", related_name="bookreviews", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    category_BookReview = models.ForeignKey(
        "Category_BookReview",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="curriculums",
    )
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_clubs:detail", kwargs={"pk": self.pk})
