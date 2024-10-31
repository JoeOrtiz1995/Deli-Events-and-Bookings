# Generated by Django 4.2.16 on 2024-10-31 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('event_date', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Unconfirmed'), (1, 'Approved')], default=0)),
                ('excerpt', models.TextField(blank=True)),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
