# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DxDetail(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    pid = models.CharField(primary_key=True, max_length=255)
    article = models.TextField()
    tags = models.TextField()

    class Meta:
        managed = False
        db_table = 'xdl_dx_special_detail'


class DxIndex(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.TextField()

    class Meta:
        managed = False
        db_table = 'xdl_dx_special_index'


class DxList(models.Model):
    pid = models.CharField(max_length=16)
    href = models.CharField(primary_key=True,unique=True, max_length=255,db_column='href_id')
    title = models.CharField(max_length=255)
    description = models.TextField()
    imgurl = models.TextField(db_column='imgUrl')  # Field name made lowercase.
    author = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'xdl_dx_special_list'
