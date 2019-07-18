# Generated by Django 2.2.3 on 2019-07-18 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Villager', '0007_auto_20190719_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('remark', models.TextField(max_length=1000)),
                ('villager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Villager.Villager')),
            ],
        ),
    ]
