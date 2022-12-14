# Generated by Django 4.0 on 2022-08-18 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UdId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128, unique=True, verbose_name='内容')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='udids', to='User.customuser')),
            ],
            options={
                'verbose_name': 'UdId',
                'verbose_name_plural': 'UdIds',
                'ordering': ['-create_date'],
            },
        ),
    ]
