from django.db import models
from django.db.models.fields import URLField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel




class GenericPage(Page):
  banner_title = models.CharField(max_length=100, default='GENERIC PAGE!')
  introduction = models.TextField(null=True, blank=True)

  banner_image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name='+',
  )
  author = models.ForeignKey(
    'Author',
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name='+',
  )
  body = StreamField(
    [
      # SAMPLE
      # ('name', blocks.SomethingBlock()),
      # ('heading', blocks.CharBlock()),
      ('heading', blocks.CharBlock(template='heading_block.html')),
      ('image', ImageChooserBlock()),
      ('paragraph', blocks.RichTextBlock()),
    ],
    null=True,
  )

  content_panels = Page.content_panels + [
    FieldPanel('banner_title'),
    FieldPanel('introduction'),
    ImageChooserPanel('banner_image'),
    SnippetChooserPanel('author'),
    StreamFieldPanel('body'),
  ]



@register_snippet
class Author(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100, blank=True)
  company_name = models.CharField(max_length=100, blank=True)
  company_url = URLField(blank=True)
  image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name='+',
  )

  panels = [
      FieldPanel('name'),
      FieldPanel('title'),
      FieldPanel('company_name'),
      FieldPanel('company_url'),
      ImageChooserPanel('image'),
  ]

  def __str__(self):
    return self.name

