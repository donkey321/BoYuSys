from tabnanny import verbose
from venv import create
from django.db import models
from User.models import CustomUser
# Create your models here.
class UdId(models.Model):
    """UdId存储"""
    content = models.CharField(max_length=128, verbose_name='内容', unique=True)
    remark = models.CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    create_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='udids')

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-create_date']
        verbose_name = 'UdId'
        verbose_name_plural = 'UdIds'