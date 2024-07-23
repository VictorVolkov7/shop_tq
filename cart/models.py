from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product
from users.models import User


class CartItem(models.Model):
    """
    CartItem model.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
    )
    cart = models.ForeignKey(
        'ShoppingCart',
        on_delete=models.CASCADE,
        verbose_name=_('Cart'),
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Quantity'),
    )

    def __str__(self):
        return f'{self.product} - {self.quantity}'

    class Meta:
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')


class ShoppingCart(models.Model):
    """
    Shopping cart model.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name=_('User')
    )
    items = models.ManyToManyField(
        Product,
        through=CartItem,
        blank=True,
        verbose_name=_('Product')
    )
    total_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Total quantity'),
    )
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name=_('Total cost')
    )

    def __str__(self):
        return f'{self.total_quantity} - {self.total_cost}'

    def calculate_totals(self) -> None:
        """
        Calculate total cost and total quantity.
        :return: None
        """
        cart_items = CartItem.objects.filter(cart=self)
        total_quantity = sum(item.quantity for item in cart_items)
        total_cost = sum(item.quantity * item.product.price for item in cart_items)

        self.total_quantity = total_quantity
        self.total_cost = total_cost
        self.save()

    class Meta:
        verbose_name = _('Shopping cart')
        verbose_name_plural = _('Shopping carts')
