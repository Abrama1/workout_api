from django.db import models


class Exercise(models.Model):
    """Model representing a predefined exercise"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    target_muscle = models.CharField(max_length=100)