from django.db import models

class Exercise(models.Model):
    description = models.CharField(max_length=255)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Wod(models.Model):
    wod_date = models.DateField('WOD Date')
    description = models.CharField(max_length=255)
    duration = models.IntegerField()


class WodExercise(models.Model):
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    rounds = models.JSONField()
    duration = models.IntegerField()
    notes = models.TextField()