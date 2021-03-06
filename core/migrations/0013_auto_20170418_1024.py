# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170417_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.wagtailcore.fields.StreamField([('featured_section', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock()), (b'link_title', wagtail.wagtailcore.blocks.CharBlock()), (b'featured_link', wagtail.wagtailcore.blocks.CharBlock()), (b'featured_page', wagtail.wagtailimages.blocks.ImageChooserBlock())]))], null=True, blank=True),
        ),
    ]
