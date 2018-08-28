# Generated by Django 2.1 on 2018-08-27 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamuserrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='process',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='process', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(through='teams.TeamUserRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
