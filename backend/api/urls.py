from django.urls import path
from . import views

# API endpoints
urlpatterns = [
    path("", views.getMessages),        # Get recent messages
    path("post/", views.postMessage)    # Post
]