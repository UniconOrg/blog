import uuid

from django.db import models
from django.utils import timezone


class UniconBlogBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    is_removed = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.id}"
