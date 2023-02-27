# Generated by Django 4.1.7 on 2023-02-27 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Recipe name')),
                ('ingredients', models.TextField(null=True)),
                ('calories', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
                ('favourites', models.ManyToManyField(blank=True, related_name='favourites', to='users.profile')),
                ('tag', models.ManyToManyField(blank=True, to='plans.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Plan name')),
                ('description', models.TextField(null=True)),
                ('calories', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('personal_plan', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
                ('recipes', models.ManyToManyField(blank=True, to='plans.recipe')),
                ('tag', models.ManyToManyField(blank=True, to='plans.tag')),
            ],
        ),
    ]