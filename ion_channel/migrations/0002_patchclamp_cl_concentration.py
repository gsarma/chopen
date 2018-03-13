# Generated by Django 2.0.3 on 2018-03-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ion_channel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patchclamp',
            name='Cl_concentration',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Initial molar concentration of Chloride (mM)'),
        ),
    ]