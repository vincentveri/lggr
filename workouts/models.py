from django.db import models

class Exercise(models.Model):
    description = models.CharField(max_length=255)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description

class Wod(models.Model):
    wod_date = models.DateField('WOD Date')
    description = models.CharField(max_length=255, null=True)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.wod_date)


class WodExercise(models.Model):
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    rounds = models.JSONField(null=True)
    duration = models.IntegerField(default=0)
    notes = models.TextField(null=True)