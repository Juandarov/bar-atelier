from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Services(models.Model):

    image = models.FileField(upload_to="services_images", null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Services"

# Pour supprimer l'image dans le dossier depuis l'admin
@receiver(pre_delete, sender=Services)
def services_delete(sender, instance, **kwargs):

    instance.image.delete(False)