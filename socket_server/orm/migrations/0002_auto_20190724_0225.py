# Generated by Django 2.2.3 on 2019-07-24 02:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('token', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('ONL', 'Online'), ('OFF', 'Offline'), ('COR', 'Corrupted'), ('DAM', 'Dammaged')], default='OFF', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='room',
            name='member',
        ),
        migrations.AddField(
            model_name='room',
            name='member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
