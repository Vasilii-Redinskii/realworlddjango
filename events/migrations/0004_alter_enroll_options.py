# Generated by Django 4.0.5 on 2022-06-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_feature_enroll_event_features'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enroll',
            options={'verbose_name': 'Записи на событие', 'verbose_name_plural': 'Запись на событие'},
        ),
    ]