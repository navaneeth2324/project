# Generated by Django 2.2.2 on 2019-06-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_author_genre_novel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='total_Novels_written',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=1),
        ),
    ]
