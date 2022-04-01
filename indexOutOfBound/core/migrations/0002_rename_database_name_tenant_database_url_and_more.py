# Generated by Django 4.0.3 on 2022-03-31 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='database_name',
            new_name='database_url',
        ),
        migrations.AddField(
            model_name='tenant',
            name='domain_url',
            field=models.CharField(default='a', max_length=300),
            preserve_default=False,
        ),
    ]
