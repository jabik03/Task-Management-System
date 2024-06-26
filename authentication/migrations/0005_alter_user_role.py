# Generated by Django 5.0.6 on 2024-06-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('manager', 'Менеджер'), ('executor', 'Исполнитель'), ('reader', 'Читатель')], default='reader', max_length=15),
        ),
    ]
