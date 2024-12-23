from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Books, Reviews
from decimal import Decimal

@receiver(post_save, sender=Reviews)
def update_book_rating_on_save(sender, instance, **kwargs):
    """
    Sharh qo'shilganda yoki yangilanganida kitobning o'rtacha reytingini yangilash.
    """
    instance.book.update_average_rating()

@receiver(post_delete, sender=Reviews)
def update_book_rating_on_delete(sender, instance, **kwargs):
    """
    Sharh o'chirilganda kitobning o'rtacha reytingini yangilash.
    """
    instance.book.update_average_rating()
