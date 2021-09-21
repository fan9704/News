# Generated by Django 3.2.7 on 2021-09-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catego', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('pubtime', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('press', models.IntegerField(default=0)),
            ],
        ),
    ]