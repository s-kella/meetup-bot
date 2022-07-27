# Generated by Django 4.0.6 on 2022-07-27 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_alter_meeting_speakers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='section',
            field=models.ForeignKey(limit_choices_to={'is_speaker': True}, on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='meetup.section', verbose_name='Секция'),
        ),
    ]
