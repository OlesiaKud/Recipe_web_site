# Generated by Django 5.1.4 on 2024-12-24 01:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('steps_cooking', models.TextField()),
                ('time_cooking', models.TextField()),
                ('image', models.ImageField(upload_to='recipe/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='recipeapp.categoryrecipe')),
                ('recipes', models.ManyToManyField(to='recipeapp.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.user'),
        ),
    ]
