# Generated by Django 4.0.1 on 2022-01-31 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0002_alter_employee_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product/category/sub'),
            preserve_default=False,
        ),
    ]