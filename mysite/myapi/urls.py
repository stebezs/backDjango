from . import views
from .views import LaunchDetailView, LaunchesListView
from django.urls import include, path

urlpatterns = [
    path('upcoming/', views.upcoming_launches, name='upcoming'),
    path('past/', views.past_launches, name='past'),
    path('next/', views.next_launch, name='next'),
    path('latest/', views.latest_launch, name='latest'),
    path('', LaunchesListView.as_view()),
]
