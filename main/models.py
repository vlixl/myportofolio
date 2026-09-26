from django.db import models
import calendar

# Create your models here.
import uuid
from django.db import models

from django.contrib.auth.models import User

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
    MONTH_CHOICES = [
        (number, calendar.month_name[number])
        for number in range(1, 13)
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    award = models.CharField(max_length=255)
    award_label = models.CharField(max_length=255) 

    category = models.CharField(max_length=255)
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    year = models.PositiveSmallIntegerField()
    
    event = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)

    description = models.TextField()
    
    def __str__(self):
        return f"{self.award} {self.award_label}, {self.category}"

class Photo(models.Model):
    
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    track = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    
    # satu proyek bisa di-star banyak pengguna,
    # dan satu pengguna bisa mem-star banyak proyek
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )
    def __str__(self):
        return self.title

    class Meta:
        permissions=[
            ("can_star_project", "Can Star Project"),
        ]