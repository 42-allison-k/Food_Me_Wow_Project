# Generated by Django 4.0 on 2022-06-25 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('food_review', '0002_seed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(help_text='The user who wrote the comment', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
