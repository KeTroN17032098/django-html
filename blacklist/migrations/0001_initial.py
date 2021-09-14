# Generated by Django 3.2.7 on 2021-09-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('no', models.AutoField(default=1, primary_key=True, serialize=False, unique=True)),
                ('kolasid', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=1)),
                ('detail', models.TextField(blank=True)),
                ('first', models.DateField(auto_now_add=True)),
                ('recent', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
