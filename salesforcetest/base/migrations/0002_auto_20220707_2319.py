# Generated by Django 3.0.14 on 2022-07-07 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='aId',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='oId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uId',
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='AccountId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Account'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='OwnerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.User'),
        ),
    ]