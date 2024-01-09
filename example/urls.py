from django.urls import path

from example.views import IndexListView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
]
