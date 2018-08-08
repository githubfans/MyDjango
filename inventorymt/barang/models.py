from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """docstring for Topic"""
    id = models.AutoField(primary_key=True, unique=True)
    kodebarang = models.CharField(max_length=30, editable=False)
    namabarang = models.CharField(max_length=30)
    deskripsi = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(null=True, editable=False)
    created_by = models.ForeignKey(User, null=True, editable=False)

    auto_create_schema = True

    def __str__(self):
        return self.namabarang
