# Generated by Django 3.2.7 on 2021-10-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baker', '0007_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
