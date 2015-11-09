# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='age',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='disability',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='education',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='ethnicity',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='familyStatus',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='gender',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='genderExpression',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='geography',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='gradeLevel',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='illustrator',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='income',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(null=True, max_length=13),
        ),
        migrations.AddField(
            model_name='book',
            name='listTitle',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='nameOfReader',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='notesByReader',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='readingLevel',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='religion',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='sexualOrientation',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='source',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(null=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(null=True, max_length=1000),
        ),
    ]
