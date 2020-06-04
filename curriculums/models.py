from django.db import models
from core import models as core_models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(AbstractItem):
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="cover_photos")
    room = models.ForeignKey("Curriculum", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Curriculum(core_models.TimeStampedModel):
    """ Curriculum Model Definition """

    title = models.CharField(max_length=50)
    sub_title = models.TextField()
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="curriculums",
    )
    description = RichTextUploadingField()
    recommendation = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    today = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("curriculums:detail", kwargs={"pk": self.pk})

    def cover_photo(self):
        (photo,) = self.photo_set.all()[:1]
        return photo.file.url
