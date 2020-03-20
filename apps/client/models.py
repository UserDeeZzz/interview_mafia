from django.db import models


# Create your models here.


class LeaderBoard(models.Model):

    client = models.CharField("客户端", max_length=20, primary_key=True)
    score = models.IntegerField("分数", default=0, null=False)

    class Meta:
        verbose_name = '排行榜'
        verbose_name_plural = '排行榜'


