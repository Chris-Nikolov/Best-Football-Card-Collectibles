# Generated by Django 5.1.3 on 2024-12-01 13:10

import cloudinary.models
import django.core.validators
import django.db.models.deletion
import djangoBestFootballCardCollectibles.cards.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(validators=[django.core.validators.MaxLengthValidator(200)], verbose_name='Title')),
                ('description', models.TextField(validators=[django.core.validators.MaxLengthValidator(2000)], verbose_name='Description')),
                ('is_for_sale', models.BooleanField(default=False, verbose_name='For Sale')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Price')),
                ('brand', models.CharField(choices=[('Topps', 'Topps'), ('Panini', 'Panini'), ('Futera', 'Futera'), ('Other', 'Other')], verbose_name='Brand')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=True, verbose_name='Approved')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[djangoBestFootballCardCollectibles.cards.validators.validate_image_size], verbose_name='image')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
    ]
