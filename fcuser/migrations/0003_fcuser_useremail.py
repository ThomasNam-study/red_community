# Generated by Django 3.0.7 on 2020-06-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20200608_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='', max_length=128, verbose_name='사용자 이메일'),
            preserve_default=False,
        ),
    ]