# Generated by Django 3.2.2 on 2021-08-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('marvel_id', models.PositiveIntegerField(default=1, unique=True, verbose_name='marvel ids')),
                ('title', models.CharField(default='', max_length=120, verbose_name='titles')),
                ('description', models.TextField(default='', verbose_name='descriptions')),
                ('price', models.FloatField(default=0.0, max_length=5, verbose_name='prices')),
                ('stock_qty', models.PositiveIntegerField(default=0, verbose_name='stock qty')),
                ('picture', models.URLField(default='', verbose_name='pictures')),
            ],
        ),
    ]