from django.db import models


class EventLog(models.Model):
    action = models.TextField()
    metadata = models.TextField()
    timestamp = models.CharField(max_length=13)
    timestamp_server = models.CharField(max_length=13)
    client_agent = models.TextField()
    client_ip = models.TextField()

    def __str__(self):
        return self.action
