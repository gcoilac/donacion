from django.db import models


class BaseModel(models.Model):
    # attributes
    id = models.BigAutoField(verbose_name="ID", primary_key=True, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
