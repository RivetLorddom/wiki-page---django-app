from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("new", views.new_page, name="new"),
    path("", views.index, name="index"),
    path("random", views.random_entry, name="random"),
    path("wiki/<str:name>", views.entry, name="entry"),
]
# For some reason changing the order of the paths above makes the app break (random page not working).
# I need to get to the bottom of it - just a reminder for my future self - riv