# Generated by Django 2.2.1 on 2019-05-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isportbook_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
