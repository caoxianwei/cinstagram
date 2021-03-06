# Generated by Django 3.0.1 on 2020-01-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_settings', '0003_auto_20200127_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinstagramusersettings',
            old_name='remainder_emails',
            new_name='reminder',
        ),
        migrations.AlterField(
            model_name='cinstagramusersettings',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='cinstagramusersettings',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cinstagramusersettings',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cinstagramusersettings',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cinstagramusersettings',
            name='personal_url',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cinstagramusersettings',
            name='phone_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
