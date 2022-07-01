# Generated by Django 3.2.13 on 2022-06-30 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/player')),
                ('dob', models.DateField()),
                ('address_line1', models.CharField(max_length=180)),
                ('address_line2', models.CharField(blank=True, max_length=180, null=True)),
                ('city', models.CharField(max_length=40)),
                ('district_county', models.CharField(max_length=20)),
                ('parent1', models.CharField(max_length=180)),
                ('parent2', models.CharField(blank=True, max_length=180, null=True)),
                ('mobile1', models.CharField(max_length=15)),
                ('mobile2', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=70)),
                ('height', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
                ('sex', models.CharField(choices=[('male', 'Băiat'), ('female', 'Fată')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
