# Generated by Django 2.0.5 on 2018-12-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview_video',
            field=models.FileField(blank=True, upload_to='preview_videos'),
        ),
    ]