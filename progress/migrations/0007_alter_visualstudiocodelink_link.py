# Generated by Django 3.2.11 on 2022-01-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0006_alter_visualstudiocodelink_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualstudiocodelink',
            name='Link',
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]