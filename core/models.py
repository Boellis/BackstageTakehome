from django.db import models

class RequestStat(models.Model):
    number: int = models.PositiveSmallIntegerField(primary_key=True) # Primary key for the number
    occurrences: int = models.PositiveIntegerField(default=0) # Number of times the number has been requested
    last_requested: models.DateTimeField = models.DateTimeField(auto_now=True) # Timestamp of the last request

    def __str__(self) -> str:
        return f"#{self.number} — {self.occurrences} queries" 