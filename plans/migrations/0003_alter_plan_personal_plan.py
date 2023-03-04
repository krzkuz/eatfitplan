# Generated by Django 4.1.7 on 2023-03-03 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_email'),
        ('plans', '0002_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='personal_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
