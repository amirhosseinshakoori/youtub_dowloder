# Generated by Django 4.2.5 on 2023-10-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveUrloath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Youtub link')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]