# Generated by Django 3.2.3 on 2021-06-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210605_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('Fashion', 'Fashion '), ('Food', 'Food'), ('Travel', 'Travel'), ('Music', 'Music'), ('Lifestyle', 'Lifestyle'), ('Fitness', 'Fitness'), ('DIY', 'DIY'), ('Sports', 'Sports'), ('Political', 'Political'), ('Tech', 'Tech'), ('Gaming', 'Gaming'), ('Pet', 'Pet')], default=None, max_length=50),
        ),
    ]
