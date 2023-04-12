# Generated by Django 3.2.9 on 2022-01-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_app', '0008_auto_20220119_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_feature_image', models.ImageField(blank=True, null=True, upload_to='home_images', verbose_name=' Home Feature Image')),
            ],
        ),
        migrations.AlterField(
            model_name='background',
            name='first_background_details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='background',
            name='first_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='background_image'),
        ),
        migrations.AlterField(
            model_name='background',
            name='first_background_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='background',
            name='second_background_details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='background',
            name='second_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='background_image'),
        ),
        migrations.AlterField(
            model_name='background',
            name='second_background_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='background',
            name='third_background_details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='background',
            name='third_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='background_image'),
        ),
        migrations.AlterField(
            model_name='background',
            name='third_background_title',
            field=models.CharField(default='', max_length=255),
        ),
    ]