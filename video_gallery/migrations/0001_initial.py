# Generated by Django 3.2 on 2022-12-05 10:18

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('tag', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=1000)),
                ('Video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tag.tag')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'VideoGallery',
                'ordering': ('created',),
            },
        ),
    ]
