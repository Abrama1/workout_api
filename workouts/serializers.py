from rest_framework import serializers
from .models import WorkoutPlan, WorkoutPlanExercise, Exercise


class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkoutPlanExercise model.
    Handles the exercises added to a workout plan
    """
    class Meta:
        model = WorkoutPlanExercise
        fields = ['exercise', 'sets', 'repetitions', 'duration']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkoutPlan model
    Allows users to create workout plans with multiple exercises
    """

    exercises = WorkoutPlanExerciseSerializer(many=True)  # Allows adding multiple exercises at once

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'user', 'name', 'exercises', 'created_at']
        read_only_fields = ['user', 'created_at']


    def create(self, validated_data):
        """
        Create a workout plan with multiple exercises
        """

        exercises_data = validated_data.pop('exercises')
        workout_plan = WorkoutPlan.objects.create(**validated_data)

        # Save each exercise with its details
        for exercise_data in exercises_data:
            WorkoutPlanExercise.objects.create(workout_plan=workout_plan, **exercise_data)

        return workout_plan