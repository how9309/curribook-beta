from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, TemplateView

from . import models, forms
from .forms import CreatorApplicationForm
from django.conf import settings

from django.core.mail import send_mail


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Curriculum
    ordering = "-created"
    context_object_name = "curriculums"  # object_list 이름 바꾸기

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["banner"] = models.Curriculum.objects.filter(today=True)[:1]
        context["recommendation"] = models.Curriculum.objects.filter(recommendation=True).order_by("-created")[:3]
        context["popular"] = models.Curriculum.objects.filter(popular=True).order_by("-created")[:5]
        context["new"] = models.Curriculum.objects.filter(new=True).order_by("-created")[:5]
        return context


class TravelView(ListView):
    model = models.Curriculum
    ordering = "-created"
    context_object_name = "curriculums"
    template_name = "curriculums/travel.html"

    def get_context_data(self, **kwargs):
        context = super(TravelView, self).get_context_data(**kwargs)
        context["travels"] = models.Curriculum.objects.filter(category="1").order_by("-created")
        return context


class KnowledgeView(ListView):
    model = models.Curriculum
    ordering = "-created"
    context_object_name = "curriculums"
    template_name = "curriculums/knowledge.html"

    def get_context_data(self, **kwargs):
        context = super(KnowledgeView, self).get_context_data(**kwargs)
        context["knowledges"] = models.Curriculum.objects.filter(category="2").order_by("-created")
        return context


class LifestyleView(ListView):
    model = models.Curriculum
    ordering = "-created"
    context_object_name = "curriculums"
    template_name = "curriculums/lifestyle.html"

    def get_context_data(self, **kwargs):
        context = super(LifestyleView, self).get_context_data(**kwargs)
        context["lifestyles"] = models.Curriculum.objects.filter(category="4").order_by("-created")
        return context


class FictionView(ListView):
    model = models.Curriculum
    ordering = "-created"
    context_object_name = "curriculums"
    template_name = "curriculums/fiction.html"

    def get_context_data(self, **kwargs):
        context = super(FictionView, self).get_context_data(**kwargs)
        context["fictions"] = models.Curriculum.objects.filter(category="3").order_by("-created")
        return context


class CurriculumDetail(DetailView):
    """ CurriculumDetail Definition """

    model = models.Curriculum


class NavView(TemplateView):
    template_name = "partials/nav.html"


class SearchView(View):
    def get(self, request):
        global curriculums
        title = request.GET.get("title")
        if title:
            form = forms.SearchForm(request.GET)

            if form.is_valid():

                title = form.cleaned_data.get("title")

                if title is not None:
                    qs = models.Curriculum.objects.filter(title__icontains=title) | models.Curriculum.objects.filter(
                        sub_title__icontains=title).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                curriculums = paginator.get_page(page)

                return render(
                    request,
                    "curriculums/search.html",
                    {
                        "form": form,
                        "curriculums": curriculums,
                        "title": title,
                        "qs": qs,
                    },
                )
        else:
            form = forms.SearchForm()

        return render(request, "curriculums/search.html", {"form": form})


def post(request):
    if request.method == "POST":
        form = CreatorApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            title = form.cleaned_data["title"]
            message = form.cleaned_data["message"]
            body = f"이름:{name} + 이메일:{email} + 내용:{message}"
            send_mail(title, body, settings.EMAIL_FROM, ["how9309@naver.com"], fail_silently=False, )
            return redirect("curriculums:application")
    else:
        form = CreatorApplicationForm()
    return render(request, 'curriculums/creator_application.html', {'form': form})
