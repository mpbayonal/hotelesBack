# Generated by Django 3.0.3 on 2020-03-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='nombre',
            field=models.CharField(default='habitacion', max_length=100),
            preserve_default=False,
        ),
    ]