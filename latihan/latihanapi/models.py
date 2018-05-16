from django.db import models
from django.contrib.auth.models import User


class PostCategory(models.Model):
    """docstring for Topic"""
    cid = models.AutoField(primary_key=True, unique=True)
    nama_kategori = models.CharField(max_length=30)
    deskripsi_kategori = models.CharField(max_length=200)
    updated_at = models.DateTimeField(null=True, editable=False)
    created_by = models.ForeignKey(User, null=True, editable=False)

    def __str__(self):
        return self.nama_kategori


class Post(models.Model):
    """docstring for Topic"""
    id = models.AutoField(primary_key=True, unique=True)
    kode_barang = models.CharField(max_length=30, editable=False)
    kategori = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length=30)
    deskripsi = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True, editable=False)
    created_by = models.ForeignKey(User, null=True, editable=False)

    def __str__(self):
        return self.nama_barang
