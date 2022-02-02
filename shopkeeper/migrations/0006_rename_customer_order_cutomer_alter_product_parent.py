# Generated by Django 4.0.1 on 2022-02-01 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0005_rename_cutomer_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='cutomer',
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ParentCategory', to='shopkeeper.parentcategory'),
        ),
    ]
