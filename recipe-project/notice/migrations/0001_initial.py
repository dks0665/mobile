# Generated by Django 3.0 on 2019-12-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('작성자', models.CharField(max_length=30, null=True)),
                ('작성일', models.DateTimeField()),
                ('제목', models.CharField(max_length=100, null=True)),
                ('내용', models.TextField()),
            ],
        ),
    ]