# Generated by Django 4.2 on 2024-04-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebCook', '0003_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes'),
        ),
    ]