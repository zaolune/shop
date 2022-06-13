# Generated by Django 3.2.4 on 2022-02-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20220210_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('unfulfilled', 'unfulfilled'), ('fulfilled', 'fulfilled'), ('canceled', 'canceled'), ('shipped', 'shipped'), ('refund', 'refund'), ('received', 'received')], default='unfulfilled', max_length=32),
        ),
    ]