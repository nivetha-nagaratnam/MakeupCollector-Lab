# Generated by Django 3.1.1 on 2020-11-11 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201111_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('makeup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.makeup')),
            ],
        ),
    ]
