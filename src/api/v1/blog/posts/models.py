from django.db import models

from core.models import UniconBlogBaseModel


class Posts(UniconBlogBaseModel):

    data = models.CharField(max_length=255, blank=True, default="")


    class Meta:
        db_table = "posts"

