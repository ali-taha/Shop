# Generated by Django 4.0 on 2021-12-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0002_basket_count_items_alter_basket_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('con', 'Confirmed'), ('rev', 'Review'), ('can', 'Canceled'), ('pai', 'Paid')], default='rev', max_length=3),
        ),
    ]
