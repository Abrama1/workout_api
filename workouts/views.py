from rest_framework import generics, permissions
from .models import WorkoutPlan
from .serializers import WorkoutPlanSerializer

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
