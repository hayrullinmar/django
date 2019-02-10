# Generated by Django 2.1.5 on 2019-02-09 10:21

from django.db import migrations, models
import django.db.models.deletion

from objectid.models import Artwork


def fix_artwork_owner(apps, schema_editor):
    artworks = Artwork.objects.all()
    for art in artworks:
        art.owner = None
        art.save()
        print("Saved")

class Migration(migrations.Migration):

    dependencies = [
        ('users', '__latest__'),
        ('objectid', '0002_artwork_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.ContentProvider'),
        ),
        migrations.RunPython(fix_artwork_owner),
    ]
