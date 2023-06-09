# Generated by Django 4.2 on 2023-04-14 22:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_options_remove_menu_active_menu_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={},
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='link',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='order',
        ),
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(default=datetime.datetime(2023, 4, 15, 3, 54, 18, 49415), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
    ]
