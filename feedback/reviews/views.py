from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView #TemplateView it's specifically focused on allowing you to build view classes that render templates.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"

    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def thank_you(request):
    return render(request, "reviews/thank_you.html")


class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    #def get_queryset(self):
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gt=4)
    #    return data


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
