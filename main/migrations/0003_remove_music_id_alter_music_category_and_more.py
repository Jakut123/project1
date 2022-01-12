# Generated by Django 4.0 on 2022-01-12 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_post_comment_music_remove_music_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='id',
        ),
        migrations.AlterField(
            model_name='music',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to='main.category'),
        ),
        migrations.AlterField(
            model_name='music',
            name='title',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
