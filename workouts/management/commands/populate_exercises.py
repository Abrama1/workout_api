from django.core.management.base import BaseCommand
from workouts.models import Exercise

class Command(BaseCommand):
    help = 'Populate the database with predefined exercises'

    def handle(self, *args, **kwargs):
        exercises = [
            {"name": "Push-up", "description": "Upper body exercise", "target_muscle": "Chest"},
            {"name": "Squat", "description": "Lower body exercise", "target_muscle": "Legs"},
            {"name": "Deadlift", "description": "Full-body strength exercise", "target_muscle": "Back"},
            {"name": "Pull-up", "description": "Back and biceps", "target_muscle": "Back"},
            {"name": "Bench Press", "description": "Chest workout", "target_muscle": "Chest"},
            {"name": "Plank", "description": "Core stability", "target_muscle": "Core"},
            {"name": "Lunges", "description": "Leg strength", "target_muscle": "Legs"},
            {"name": "Bicep Curl", "description": "Biceps", "target_muscle": "Arms"},
            {"name": "Tricep Dips", "description": "Triceps", "target_muscle": "Arms"},
            {"name": "Leg Press", "description": "Leg muscle", "target_muscle": "Legs"},
            {"name": "Shoulder Press", "description": "Overhead pressing exercise", "target_muscle": "Shoulders"},
            {"name": "Lat Pulldown", "description": "Lat and back muscle exercise", "target_muscle": "Back"},
            {"name": "Hammer Curl", "description": "Biceps and forearms", "target_muscle": "Arms"},
            {"name": "Hip Thrust", "description": "Glute activation", "target_muscle": "Glutes"},
            {"name": "Russian Twists", "description": "Oblique exercise", "target_muscle": "Core"},
            {"name": "Calf Raise", "description": "Strengthens calf muscles", "target_muscle": "Legs"},
            {"name": "Face Pull", "description": "Rear delts and traps", "target_muscle": "Shoulders"},
            {"name": "Hanging Leg Raises", "description": "Lower abs", "target_muscle": "Core"},
            {"name": "Chest Fly", "description": "Isolation exercise for chest", "target_muscle": "Chest"},
            {"name": "Romanian Deadlift", "description": "Hamstring and glutes", "target_muscle": "Legs"},
        ]

        for exercise in exercises:
            Exercise.objects.get_or_create(**exercise)

        self.stdout.write(self.style.SUCCESS('Successfully populated exercises!'))
