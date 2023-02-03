# Generated by Django 3.2.16 on 2023-02-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motor_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=100)),
                ('hp', models.IntegerField(blank=True, null=True)),
                ('others', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('hsncode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='other_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('specifications', models.CharField(max_length=50)),
                ('hsncode', models.CharField(max_length=50)),
            ],
        ),
    ]
