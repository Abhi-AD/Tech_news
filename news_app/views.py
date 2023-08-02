from django.views.generic import ListView,View,TemplateView
from news_app.models import Post, Category, Tag,Review
from django.shortcuts import render


# Create your views here.
class HomeView(ListView):
    model = Post  # specify the data source for this view (Post)
    template_name = "tech/tech-index.html"  # set a custom HTML file to use as our
    context_object_name = "posts"
    queryset = Post.objects.filter(
        published_at__isnull=False, status="published"
    ).order_by("-published_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = (
            Post.objects.filter(published_at__isnull=False, status="published")
            .order_by("-published_at", "-view_count")
            .first()
        )
        context["sections"] = Post.objects.filter(
            published_at__isnull=False, status="published"
        ).order_by("-published_at", "-view_count")[1:3]

        context["recent_posts"] = Post.objects.filter(
            published_at__isnull=False, status="published"
        ).order_by("-published_at")[:5]
        
        context['reviews_posts'] = Post.objects.filter(
            published_at__isnull=False, status="published"
        ).order_by("-published_at")[:5]
        return context

class ContactView(TemplateView):
    template_name = "tech/tech-contact.html"
