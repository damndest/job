# Generated by Django 4.0.4 on 2024-05-31 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_rename_team_id_sportsplayer_player_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportspost',
            name='post_author_nn',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
    ]
