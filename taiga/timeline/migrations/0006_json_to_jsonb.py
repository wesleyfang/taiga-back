# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 11:35
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_auto_20160706_0723'),
    ]

    operations = [
        migrations.RunSQL(
            """
                ALTER TABLE "{table_name}"
                   ALTER COLUMN "{column_name}"
                           TYPE jsonb
                          USING to_json("{column_name}"::text)::jsonb;
            """.format(
                table_name="timeline_timeline",
                column_name="data",
            ),
            reverse_sql=migrations.RunSQL.noop
        ),
    ]
