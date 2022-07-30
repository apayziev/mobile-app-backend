from django.urls import path
from course.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]