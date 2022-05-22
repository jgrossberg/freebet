# Generated by Django 4.0.4 on 2022-05-22 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0004_remove_bet_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='line',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='betting.line'),
            preserve_default=False,
        ),
    ]