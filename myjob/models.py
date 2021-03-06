# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class YiqingTestTabel3(models.Model):
    dateline = models.CharField(primary_key=True, max_length=255)
    usernum = models.BigIntegerField(blank=True, null=True)
    newnum = models.BigIntegerField(blank=True, null=True)
    feifei = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        #true:可对数据表进行migrate或migrations删除等操作
        #false:不会对数据库表进行操作
        db_table = 'yiqing_test_tabel3'