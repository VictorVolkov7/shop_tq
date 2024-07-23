from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    Category model.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Category name'),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name=_('Slug'),
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name=_('Image'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class SubCategory(models.Model):
    """
    Sub Category model.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Category name'),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name=_('Slug'),
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name=_('Image'),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name=_('Category'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Sub Category')
        verbose_name_plural = _('Sub Categories')
