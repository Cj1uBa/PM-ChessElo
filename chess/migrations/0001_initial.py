# Generated by Django 4.0.3 on 2022-04-07 12:40

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
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_white', models.BooleanField(default=True)),
                ('fen', models.CharField(blank=True, max_length=100, null=True)),
                ('pgn', models.TextField(blank=True, null=True)),
                ('result', models.IntegerField(blank=True, choices=[(1, 'Winner: white'), (2, 'Winner: black'), (3, 'Draw')], default=None, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Game created'), (2, 'Game in progress'), (3, 'Game completed')], default=1)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL)),
                ('opponent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]