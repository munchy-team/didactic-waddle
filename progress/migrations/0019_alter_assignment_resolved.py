# Generated by Django 3.2.11 on 2022-01-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0018_assignment_less_important_messages_and_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='Resolved',
            field=models.CharField(choices=[('Not Yet', 'Not Yet'), ('Yes', 'Yes'), ('Postponed', 'Postponed'), ('Out The Window!(Canceled)', 'Out The Window!(Canceled)')], max_length=30),
        ),
    ]