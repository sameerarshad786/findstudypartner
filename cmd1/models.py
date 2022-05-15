from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone

class Room(models.Model):
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    roomname = models.TextField(
        max_length=30,
    )

    C = 'C'
    C_PLUS_PLUS = 'c++'
    C_SHARP = 'C#'
    PYTHON = 'PY'
    DJANGO = 'DJ'
    FLASK = 'FL'
    REACT = 'R'
    JAVA_SCRIPT = 'JS'
    GIT = 'GIT'
    WORDPRESS = 'WP'
    Topic_choices = [
        (C, 'C'),
        (C_PLUS_PLUS, 'C++'),
        (C_SHARP, 'C#'),
        (PYTHON, 'Python'),
        (DJANGO, 'Django'),
        (FLASK, 'Flask'),
        (REACT, 'React'),
        (JAVA_SCRIPT, 'Java Script'),
        (GIT, 'Git'),
        (WORDPRESS, 'Wordpress'),
    ]

    topics = models.CharField(
        max_length=11,
        choices=Topic_choices,
        default=PYTHON
    )

    about = models.TextField()

    date_posted = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return f'{self.host}'

    def get_absolute_url(self):
        return reverse('room', kwargs={'pk': self.pk})

    @property
    def calculate_time(self) -> str:
        current_date = datetime.now(timezone.utc)
        _cal = current_date - self.date_posted
        if _cal <= timedelta(seconds=10):
            return "Just Now"
        elif _cal <= timedelta(minutes=59):
            minutes = int(_cal.seconds/59)
            return f"{minutes} min"
        elif _cal <= timedelta(hours=3599):
            hours = int(_cal.seconds/3599)
            return f"{hours} hr"
        elif _cal <= timedelta(days=1):
            days = int(_cal.seconds/86376)
            return f"{days} day ago"
        else:
            return self.date_posted.strftime("%F %d, %Y")
