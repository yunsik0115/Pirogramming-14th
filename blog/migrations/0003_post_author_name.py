# Generated by Django 3.1.5 on 2021-01-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
    ]
