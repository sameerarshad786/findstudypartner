# Generated by Django 4.0.4 on 2022-05-14 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.TextField(max_length=30)),
                ('topics', models.CharField(choices=[('C', 'C'), ('c++', 'C++'), ('C#', 'C#'), ('PY', 'Python'), ('DJ', 'Django'), ('FL', 'Flask'), ('R', 'React'), ('JS', 'Java Script'), ('GIT', 'Git'), ('WP', 'Wordpress')], default='PY', max_length=11)),
                ('about', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]