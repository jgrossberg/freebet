# Generated by Django 4.0.4 on 2022-05-22 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0007_alter_line_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='betting.team'),
        ),
    ]