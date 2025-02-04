from django.urls import path
from .views import WorkoutPlanListCreateView

urlpatterns = [
    path('workout-plans/', WorkoutPlanListCreateView.as_view(), name='workout-plans'),
]