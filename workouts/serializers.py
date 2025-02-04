from rest_framework import serializers
from .models import WorkoutPlan, WorkoutPlanExercise, Exercise


class WorkoutPlanSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkoutPlan model.
    It retrieves exercises through the WorkoutPlanExercise model.
    """
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'user', 'name', 'exercises', 'created_at']
        read_only_fields = ['user', 'created_at']

    def get_exercises(self, obj):
        """
        Retrieve the exercises linked to this workout plan.
        """
        return [
            {
                "exercise": wpe.exercise.id,
                "sets": wpe.sets,
                "repetitions": wpe.repetitions,
                "duration": wpe.duration
            }
            for wpe in obj.workoutplanexercise_set.all()
        ]

    def create(self, validated_data):
        """
        Create a workout plan with multiple exercises.
        """
        exercises_data = self.initial_data.get('exercises', [])
        workout_plan = WorkoutPlan.objects.create(user=self.context['request'].user, name=validated_data['name'])

        # Save each exercise with its details
        for exercise_data in exercises_data:
            WorkoutPlanExercise.objects.create(
                workout_plan=workout_plan,
                exercise_id=exercise_data["exercise"],
                sets=exercise_data.get("sets", 3),
                repetitions=exercise_data.get("repetitions", 10),
                duration=exercise_data.get("duration")
            )

        return workout_plan
