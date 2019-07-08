# Generated by Django 2.2.3 on 2019-07-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer_app', '0007_auto_20190704_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('button_text', models.CharField(max_length=255)),
                ('button_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
