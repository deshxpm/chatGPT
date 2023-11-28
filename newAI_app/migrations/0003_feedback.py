# Generated by Django 4.2.7 on 2023-11-26 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newAI_app', '0002_chathistory_usermsg_alter_chathistory_display_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resion', models.CharField(max_length=100)),
                ('remark', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
