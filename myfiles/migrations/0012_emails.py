# Generated by Django 4.0.6 on 2022-09-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0011_delete_emails'),
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
    ]
