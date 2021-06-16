# Generated by Django 3.2.3 on 2021-06-05 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion '), ('Food', 'Food'), ('Travel', 'Travel'), ('Music', 'Music'), ('Lifestyle', 'Lifestyle'), ('Fitness', 'Fitness'), ('DIY', 'DIY'), ('Sports', 'Sports'), ('Political', 'Political'), ('Tech', 'Tech'), ('Gaming', 'Gaming'), ('Pet', 'Pet')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]