from django.views.generic import ListView, DetailView, TemplateView, FormView, UpdateView
from . import models, forms
from users import mixins as user_mixins
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render, redirect, reverse


class BookReviewView(ListView):
    """ BookReviewView Definition """

    model = models.BookReview
    ordering = "-created"
    context_object_name = "BookReviews"  # object_list 이름 바꾸기
    template_name = "book_clubs/bookReview_list.html"


class BookReviewDetail(DetailView):
    """ BookReviewDetail Definition """

    model = models.BookReview
    context_object_name = "BookReviews"  # object_list 이름 바꾸기
    template_name = "book_clubs/bookReviewDetail.html"


class BookClubListView(TemplateView):
    template_name = "book_clubs/bookClub_list.html"


class EnglandView(ListView):
    model = models.BookReview
    ordering = "-created"
    context_object_name = "BookReviews"
    template_name = "book_clubs/bookClub_england.html"

    def get_context_data(self, **kwargs):
        context = super(EnglandView, self).get_context_data(**kwargs)
        context["englands"] = models.BookReview.objects.filter(category_BookReview="1").order_by("-created")
        return context


class DogView(ListView):
    model = models.BookReview
    ordering = "-created"
    context_object_name = "BookReviews"
    template_name = "book_clubs/bookClub_dog.html"

    def get_context_data(self, **kwargs):
        context = super(DogView, self).get_context_data(**kwargs)
        context["dogs"] = models.BookReview.objects.filter(category_BookReview="2").order_by("-created")
        return context


class ConsumerView(ListView):
    model = models.BookReview
    ordering = "-created"
    context_object_name = "BookReviews"
    template_name = "book_clubs/bookClub_consumer.html"

    def get_context_data(self, **kwargs):
        context = super(ConsumerView, self).get_context_data(**kwargs)
        context["consumers"] = models.BookReview.objects.filter(category_BookReview="3").order_by("-created")
        return context


class ThinkView(ListView):
    model = models.BookReview
    ordering = "-created"
    context_object_name = "BookReviews"
    template_name = "book_clubs/bookClub_think.html"

    def get_context_data(self, **kwargs):
        context = super(ThinkView, self).get_context_data(**kwargs)
        context["thinks"] = models.BookReview.objects.filter(category_BookReview="4").order_by("-created")
        return context


class EditBookReviewView(user_mixins.LoggedInOnlyView, UpdateView):
    model = models.BookReview
    template_name = "book_clubs/bookreview_edit.html"
    fields = (
        "title",
        "sub_title",
        "category_BookReview",
        "description",
    )

    def get_object(self, queryset=None):
        Bookreview = super().get_object(queryset=queryset)
        if Bookreview.author.pk != self.request.user.pk:
            raise Http404()
        return Bookreview


class CreateBookReviewView(user_mixins.LoggedInOnlyView, FormView):
    form_class = forms.CreateBookReviewForm
    template_name = "book_clubs/bookreview_create.html"

    def form_valid(self, form):
        BookReview = form.save()
        BookReview.author = self.request.user
        BookReview.save()
        form.save_m2m()
        messages.success(self.request, "서평 작성 완료")
        return redirect(reverse("book_clubs:detail", kwargs={"pk": BookReview.pk}))
