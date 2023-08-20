# Generated by Django 4.2.3 on 2023-08-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('reader', 'Reader'), ('admin', 'Admin')], default='admin', max_length=10),
            preserve_default=False,
        ),
    ]