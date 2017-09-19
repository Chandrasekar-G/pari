# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import location.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import album.models
import resources.models
import article.streamfields.blocks
import wagtail.wagtailimages.blocks
import face.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_add_show_modular_content_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='modular_content',
            field=wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))])), ('n_column_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'paragraph', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))])))])), ('paragraph_with_map', wagtail.wagtailcore.blocks.StructBlock([(b'locations', article.streamfields.blocks.ModelMultipleChoiceBlock(target_model=location.models.Location)), (b'map_align', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))]))])), ('paragraph_with_page', wagtail.wagtailcore.blocks.StructBlock([(b'page', article.streamfields.blocks.PageTypeChooserBlock(for_models=[b'article.models.Article', album.models.Album, face.models.Face, resources.models.Resource])), (b'align_image', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))]))])), ('paragraph_with_quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_quote')), (b'align_quote', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'right', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))]))])), ('full_width_quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', article.streamfields.blocks.CustomRichTextBlock(required=True, editor=b'hallo_for_quote'))])), ('video_with_quote', wagtail.wagtailcore.blocks.StructBlock([(b'video', wagtail.wagtailembeds.blocks.EmbedBlock(help_text=b'YouTube video URL')), (b'video_caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote')), (b'quote', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_quote')), (b'align_quote', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'Left column', choices=[(b'left', b'Left column'), (b'right', b'Right column')]))])), ('image_with_quote_and_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'height', article.streamfields.blocks.IntegerBlock(default=380, min_value=0, required=True)), (b'caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote'))], required=True)), (b'align_image', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content_1', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))], required=False)), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', article.streamfields.blocks.CustomRichTextBlock(required=True, editor=b'hallo_for_quote'))], required=True)), (b'content_2', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))], required=False))])), ('full_width_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())])), (b'caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote'))])), ('columnar_image_with_text', wagtail.wagtailcore.blocks.StructBlock([(b'images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())]))), (b'height', article.streamfields.blocks.IntegerBlock(default=380, min_value=0, required=True)), (b'caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote')), (b'align_columnar_images', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))], required=False))])), ('full_width_embed', wagtail.wagtailcore.blocks.StructBlock([(b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text=b'Enter URL for the embed block', required=True)), (b'embed_caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote'))])), ('paragraph_with_embed', wagtail.wagtailcore.blocks.StructBlock([(b'embed', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'embed_caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote')), (b'embed_max_width', article.streamfields.blocks.IntegerBlock(help_text=b'Optional field. Maximum width of the content in pixels to be requested from the content provider(e.g YouTube). If the requested width is not supported, provider will be supplying the content with nearest available width.', required=False)), (b'embed_align', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))]))])), ('paragraph_with_raw_embed', wagtail.wagtailcore.blocks.StructBlock([(b'embed', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text=b'Embed HTML code(an iframe)')), (b'embed_caption', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_quote')), (b'embed_align', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left column'), (b'right', b'Right column')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', article.streamfields.blocks.CustomRichTextBlock(required=False, editor=b'hallo_for_paragraph')), (b'align_content', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'default', choices=[(b'default', b'Default'), (b'center', b'Center')]))], required=False))]))], null=True, blank=True),
        ),
    ]
