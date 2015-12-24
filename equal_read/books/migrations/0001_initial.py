# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listTitle', models.CharField(null=True, max_length=1000)),
                ('title', models.CharField(null=True, max_length=1000)),
                ('source', models.CharField(null=True, max_length=1000)),
                ('isbn', models.CharField(null=True, max_length=13)),
                ('author', models.CharField(null=True, max_length=1000)),
                ('illustrator', models.CharField(null=True, max_length=1000)),
                ('publisher', models.CharField(null=True, max_length=1000)),
                ('year', models.IntegerField(default=0)),
                ('pages', models.IntegerField(default=0)),
                ('readingLevel', models.CharField(null=True, max_length=1000)),
                ('gradeLevel', models.CharField(null=True, max_length=1000)),
                ('nameOfReader', models.CharField(null=True, max_length=1000)),
                ('gender', models.CharField(null=True, max_length=1000)),
                ('genderExpression', models.CharField(null=True, max_length=1000)),
                ('age', models.IntegerField(default=0)),
                ('ethnicity', models.CharField(null=True, max_length=1000)),
                ('disability', models.CharField(null=True, max_length=1000)),
                ('sexualOrientation', models.CharField(null=True, max_length=1000)),
                ('education', models.CharField(null=True, max_length=1000)),
                ('income', models.IntegerField(default=0)),
                ('religion', models.CharField(null=True, max_length=1000)),
                ('geography', models.CharField(null=True, max_length=1000)),
                ('familyStatus', models.CharField(null=True, max_length=1000)),
                ('notesByReader', models.CharField(null=True, max_length=1000)),
            ],
        ),
    ]
