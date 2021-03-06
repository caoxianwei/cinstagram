# Generated by Django 3.0.1 on 2020-01-22 15:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='uploaded_media/')),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('caption', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.CinstagramUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhotoLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('like_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.CinstagramUser')),
                ('liked_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_upload.UserPhoto')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhotoComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=2000)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('comment_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.CinstagramUser')),
                ('commented_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_upload.UserPhoto')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhotoBookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookmark_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.CinstagramUser')),
                ('bookmarked_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_upload.UserPhoto')),
            ],
        ),
    ]
