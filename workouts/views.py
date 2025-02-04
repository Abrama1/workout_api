from rest_framework import generics, permissions
from .models import WorkoutPlan, FitnessGoal, WeightTracking
from .serializers import WorkoutPlanSerializer, FitnessGoalSerializer, WeightTrackingSerializer


class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating workout plans.
    """

    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create workout plans

    def get_queryset(self):
        """Return only the workout plans created by the authenticated user."""

        return WorkoutPlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Asing the authenticated user to the new workout plan"""

        serializer.save(user=self.request.user)

class FitnessGoalListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating fitness goals.
    """
    serializer_class = FitnessGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return only the fitness goals of the authenticated user."""
        return FitnessGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Assign the authenticated user to the fitness goal."""
        serializer.save(user=self.request.user)

class WeightTrackingListCreateView(generics.ListCreateAPIView):
    """
    API view for tracking user weight.
    """
    serializer_class = WeightTrackingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return only the weight records of the authenticated user."""
        return WeightTracking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Assign the authenticated user to the weight entry."""
        serializer.save(user=self.request.user)
