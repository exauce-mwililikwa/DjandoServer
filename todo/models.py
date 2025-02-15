from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=25)
    done = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
