# productos/signals.py
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_admin_products_group(sender, **kwargs):
    if sender.name == 'productos':
        Group.objects.get_or_create(name='ADMIN_PRODUCTS')
