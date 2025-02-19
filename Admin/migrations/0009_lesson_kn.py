# Generated by Django 5.1.1 on 2024-10-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_remove_langap_ngay_gap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_KN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('ppt', models.FileField(blank=True, null=True, upload_to='ppts/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('vip_only', models.BooleanField(default=False)),
            ],
        ),
    ]
