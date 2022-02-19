from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name


class HomeBannerModel(models.Model):
    title = models.TextField(verbose_name=_('title'))
    collection = models.CharField(max_length=60, verbose_name=_('collection'))
    description = models.TextField(verbose_name=_('description'))
    banner = models.ImageField(upload_to='banner', verbose_name=_('banner'))
    is_active = models.BooleanField(verbose_name=_('active'), default=True)

    def __str__(self):
        return self.collection

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')
