from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import SubCategory


class Product(models.Model):
    """
    Product model.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Product name'),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name=_('Slug'),
    )
    image_s = models.ImageField(
        upload_to='products/small/',
        blank=True,
        null=True,
        verbose_name=_('Image small'),
    )
    image_m = models.ImageField(
        upload_to='products/medium/',
        blank=True,
        null=True,
        verbose_name=_('Image medium'),
    )
    image_l = models.ImageField(
        upload_to='products/large/',
        blank=True,
        null=True,
        verbose_name=_('Image large'),
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Price')
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='subcategory',
        verbose_name=_('Sub category'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
