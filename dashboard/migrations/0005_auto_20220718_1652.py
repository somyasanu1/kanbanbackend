# Generated by Django 3.2.14 on 2022-07-18 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
        ('dashboard', '0004_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
    ]