from django.db import models


class Robot(models.Model):
    """Модель робота."""

    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    class Meta:
        ordering = ('serial',)
        verbose_name = 'робот'
        verbose_name_plural = 'роботы'
        constraints = [
            models.UniqueConstraint(
                fields=['model', 'version'],
                name='unique_model_version',
            ),
        ]
