# Generated by Django 5.0.6 on 2024-06-04 01:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodReply',
            fields=[
                ('food_rpl_no', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
                ('regist_date', models.DateTimeField()),
                ('food_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
                ('member_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
