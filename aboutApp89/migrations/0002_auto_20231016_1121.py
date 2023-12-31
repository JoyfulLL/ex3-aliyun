# Generated by Django 2.2.4 on 2023-10-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutApp89', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='荣誉描述'),
        ),
        migrations.AlterField(
            model_name='award',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Award/', verbose_name='荣誉照片'),
        ),
    ]
