# Generated by Django 4.1.2 on 2023-11-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newAI_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='usermsg',
            field=models.CharField(default='dsdd', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chathistory',
            name='display_msg',
            field=models.CharField(max_length=1000),
        ),
    ]