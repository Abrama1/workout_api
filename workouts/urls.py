from django.urls import path
from .views import WorkoutPlanListCreateView, FitnessGoalListCreateView, WeightTrackingListCreateView

urlpatterns = [
    path('workout-plans/', WorkoutPlanListCreateView.as_view(), name='workout-plans'),
    path('fitness-goals/', FitnessGoalListCreateView.as_view(), name='fitness-goals'),
    path('weight-tracking/', WeightTrackingListCreateView(), name='weight-tracking'),
]