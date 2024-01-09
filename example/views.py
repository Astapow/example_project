from django.views.generic import ListView

from example.models import Example


class IndexListView(ListView):
    model = Example
    template_name = "index.html"
