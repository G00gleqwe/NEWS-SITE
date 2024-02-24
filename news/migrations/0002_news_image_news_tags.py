# Generated by Django 5.0.2 on 2024-02-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.CharField(blank=True, choices=[('Yangi', 'Yangi'), ('Dolzarb', 'Dolzarb'), ('Qaynoq', 'Qaynoq')], max_length=150, null=True),
        ),
    ]
