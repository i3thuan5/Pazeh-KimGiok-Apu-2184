from django.db import models

# Create your models here.


class Record(models.Model):
    """
    潘金玉《巴宰族母語錄音2184句》錄音基本單位。
    """
    csvid = models.PositiveIntegerField(
        default=0,
        help_text='Google Excel編號'
    )
    pazeh = models.CharField(
        db_index=True,
        max_length=255,
        help_text='Pazeh文字項目'
    )
    hua = models.CharField(
        db_index=True,
        max_length=255,
        help_text='Pazeh華語解說項目'
    )
    pageid = models.PositiveIntegerField(
        default=0,
        help_text='原始頁碼'
    )
