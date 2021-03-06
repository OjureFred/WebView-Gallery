# Generated by Django 3.0.8 on 2020-07-31 15:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['image_name']},
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='save_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_description',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='gallery',
            name='categories',
            field=models.ManyToManyField(to='gallery.categories'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='gallery.Location'),
        ),
    ]
