# Generated by Django 4.2 on 2023-04-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='region',
            field=models.CharField(choices=[('서울', '서울'), ('강원도', '강원도'), ('경기도', '경기도'), ('충청도', '충청도'), ('전라도', '전라도'), ('경상도', '경상도'), ('제주도', '제주도'), ('평양', '평양')], max_length=3),
        ),
    ]
