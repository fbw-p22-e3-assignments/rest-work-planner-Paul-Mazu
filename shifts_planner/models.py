from django.db import models
from django.contrib.auth.models import User


class Shift(models.Model):
    SHIFTS = (
        ("00:00 - 08:00", "I shift"),
        ("08:00 - 16:00", "II shift"),
        ("16:00 - 00:00", "III shift"),
    )

    date = models.DateField(blank=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.CharField(max_length=200, choices=SHIFTS, blank=True)

    class Meta:
        unique_together = [["date", "employee"]]
