# Generated by Django 2.0.5 on 2018-12-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='poster',
            field=models.ImageField(blank=True, upload_to='course_images'),
        ),
    ]
