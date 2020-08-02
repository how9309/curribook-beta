from django import forms
from . import models
from django_ckeditor_5.widgets import CKEditor5Widget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_ckeditor_5.fields import CKEditor5Field
from django_summernote.widgets import SummernoteWidget


class CreateBookReviewForm(forms.ModelForm):
    class Meta:
        model = models.BookReview
        fields = (
            "title",
            "sub_title",
            "category_BookReview",
            "description",
        )
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': '제목을 입력하세요.'}
            ),
            'sub_title': forms.TextInput(
                attrs={'placeholder': '소제목을 입력하세요.'}
            ),
            'category_BookReview': forms.Select(
                attrs={'placeholder': '카테고리', 'class': 'custom-select'},
            ),
            'description': forms.Textarea(attrs={'placeholder': '내용을 입력하세요.'})
        }

    def save(self, *args, **kwargs):
        bookreview = super().save(commit=False)
        return bookreview
