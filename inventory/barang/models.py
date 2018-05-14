from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """docstring for Topic"""
    deskripsi = models.TextField(max_length=4000)
    namabarang = models.TextField(max_length=30)
    kodebarang = models.TextField(max_length=30)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        return self.namabarang
