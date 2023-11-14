from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetbalspelers(models.Model):
    """
    Model representing football players.
    """
    name = models.CharField(max_length=200, help_text="Name of the football player")
    current_club = models.CharField(max_length=200, help_text="Current football club")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(default=timezone.now, help_text="Date of entry")
    last_modified_date = models.DateTimeField(auto_now=True, help_text="Date of last modification")

    def save_and_publish(self):
        """
        Save the entry and set the publication date to the current time.
        """
        self.save()

    def __str__(self):
        return self.name
