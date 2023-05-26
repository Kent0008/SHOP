# Generated by Django 4.2.1 on 2023-05-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('descriptions', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(default='100', verbose_name='Price')),
                ('size', models.IntegerField(default='35', verbose_name='Size')),
                ('image', models.ImageField(upload_to='Produc_img', verbose_name='Image')),
                ('gender', models.CharField(max_length=30, verbose_name='Gender')),
                ('quant', models.IntegerField(verbose_name='Quant')),
                ('create_data', models.DateTimeField(auto_now_add=True)),
                ('update_data', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.brand', verbose_name='Brand')),
            ],
        ),
    ]