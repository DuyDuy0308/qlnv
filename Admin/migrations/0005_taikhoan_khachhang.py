# Generated by Django 5.1.1 on 2024-10-19 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_alter_doi_quan_ly_alter_khachhang_doi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taikhoan',
            name='khachhang',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.khachhang'),
        ),
    ]