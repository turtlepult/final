# Generated by Django 4.2 on 2024-04-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebCook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='recipes'),
        ),
    ]