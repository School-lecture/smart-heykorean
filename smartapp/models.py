from django.db import models

class Event(models.Model):
    edate         = models.TextField()
    singer        = models.TextField()
    location      = models.TextField()
    link          = models.TextField()

class Add(models.Model):
    edate         = models.TextField()
    singer        = models.TextField()
    location      = models.TextField()
    link          = models.TextField()