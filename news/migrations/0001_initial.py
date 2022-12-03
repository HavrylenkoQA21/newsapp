# Generated by Django 4.1.3 on 2022-12-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_uk', models.CharField(max_length=100, null=True)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('about', models.TextField(max_length=256)),
                ('about_uk', models.TextField(max_length=256, null=True)),
                ('about_en', models.TextField(max_length=256, null=True)),
                ('content', models.TextField(max_length=1024)),
                ('content_uk', models.TextField(max_length=1024, null=True)),
                ('content_en', models.TextField(max_length=1024, null=True)),
                ('author', models.CharField(max_length=100)),
                ('author_uk', models.CharField(max_length=100, null=True)),
                ('author_en', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='images/')),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('source', models.URLField()),
            ],
        ),
    ]
