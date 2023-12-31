# Generated by Django 4.2.4 on 2023-08-31 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='todolist',
            name='pessoa',
            field=models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.pessoa'),
        ),
    ]
