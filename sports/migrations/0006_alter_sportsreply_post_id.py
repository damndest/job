# Generated by Django 4.0.4 on 2024-06-02 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0005_alter_sportspost_post_author_nn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsreply',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reply', to='sports.sportspost'),
        ),
    ]
