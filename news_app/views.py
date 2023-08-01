from django.views.generic import ListView
from news_app.models import Post,Category,Tag


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
        context["featured_posts"] = (
            Post.objects.filter(published_at__isnull=False, status="published")
            .order_by("-published_at").first()
        )
        context["sections"] = (
            Post.objects.filter(published_at__isnull=False, status="published")
            .order_by("-published_at")[1:3]
        )
        return context