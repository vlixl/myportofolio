from django.db import models

# Create your models here.
import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    school = models.CharField(max_length=255)

    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(null=True, blank=True)
    grade = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            null=True,
            blank=True
        )

    description = models.TextField()
    
    logo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.school

    @property
    def is_ongoing(self):
        return self.end_year is None

class Achievement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)
    event = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)

    month = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()

    description = models.TextField()
    
    def __str__(self):
        return self.title