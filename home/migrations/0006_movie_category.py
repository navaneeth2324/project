# Generated by Django 2.2.2 on 2019-06-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_movie_awards'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Category',
            field=models.CharField(choices=[(1, 'Thriller'), (2, 'Action'), (3, 'Romantic'), (4, 'Si-Fi'), (5, 'Comedy')], default=5, help_text='Movie Category', max_length=2),
        ),
    ]
