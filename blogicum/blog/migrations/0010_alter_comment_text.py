# Generated by Django 3.2.16 on 2025-05-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=400, verbose_name='Текст комментария'),
        ),
    ]
