# Generated by Django 4.2.6 on 2023-11-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_weddingmain_bride_title_weddingmain_groom_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bride_mother_account',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='groom_mother_account',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
