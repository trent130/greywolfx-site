# Generated by Django 5.0.2 on 2024-08-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticpages', '0006_subscribe_testimonial_picture_alter_testimonial_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='post',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
