# Generated by Django 4.0.4 on 2022-07-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnTradingSwiftly', '0002_rename_lessons_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(max_length=100000),
        ),
    ]
