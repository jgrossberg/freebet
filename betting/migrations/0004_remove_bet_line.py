# Generated by Django 4.0.4 on 2022-05-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0003_line_team_delete_totalline_line_team_bet_line_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='line',
        ),
    ]
