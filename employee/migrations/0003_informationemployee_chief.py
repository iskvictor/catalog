# Generated by Django 2.2.1 on 2019-05-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190526_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationemployee',
            name='chief',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
