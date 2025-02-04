from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    """Model representing a predefined exercise"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_muscle = models.CharField(max_length=100)

class WorkoutPlan(models.Model):
    """
    Model representing a user's workout plan.
    a workout plan consists of multiple exercises.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the plan
    name = models.CharField(max_length=100)  # Workout plan name
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the plan was created

    def __str__(self):
        return self.name

class WorkoutPlanExercise(models.Model):
    """
    Model to store exercises inside a workout plan
    Each workout plan can contain multiple exercises
    """
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    sets = models.IntegerField(default=3)  # Number of sets
    repetitions = models.IntegerField(default=10)  # Number of repetitions
    duration = models.IntegerField(null=True, blank=True)  # Durations in seconds (optional)

    def __str__(self):
        return f"{self.workout_plan.name} - {self.exercise.name}"

class FitnessGoal(models.Model):
    """
    Model representing a user's fitness goal.
    Users can set a goal, such as "Lose 5kg in 3 months".
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=100)  # Example: "Lose Weight"
    target_value = models.FloatField()  # Example: 70 kg
    current_value = models.FloatField()  # Example: 80 kg
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.goal_type} (Target: {self.target_value})"

class WeightTracking(models.Model):
    """
    Model for tracking a user's weight over time.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg on {self.recorded_at}"
