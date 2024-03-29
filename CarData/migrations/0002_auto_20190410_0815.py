# Generated by Django 2.1.5 on 2019-04-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=80)),
            ],
        ),
        migrations.RemoveField(
            model_name='cartransaction',
            name='model',
        ),
        migrations.AddField(
            model_name='cartransaction',
            name='car_model',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='cartransaction',
            name='make',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='cartransaction',
            name='sale_price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cartransaction',
            name='sold_by',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
