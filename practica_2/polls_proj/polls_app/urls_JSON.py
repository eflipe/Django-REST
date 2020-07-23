from django.urls import path
from .views import poll_list, poll_detail


urlpatterns = [
    path("polls/", poll_list, name="poll_list"),
    path("polls/<int:pk>", poll_detail, name="poll_detail")
]
