# Generated by Django 4.2.1 on 2023-06-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_alter_seller_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_model',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
