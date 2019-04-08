from django.db import models
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    flag = models.CharField(
        verbose_name='属性',
        max_length=200,
    )

    name = models.CharField(
        verbose_name='商品名',
        max_length=200,
    )

    TYPE_CHOICES = (
        (1, '飲み物'),
        (2, '食べ物'),
        (3, 'その他'),
    )

    type = models.IntegerField(
        verbose_name='種類',
        choices=TYPE_CHOICES,
        default=1,
    )

    count = models.IntegerField(
        verbose_name = '個数',
        validators=[validators.MinValueValidator(1)],
        blank = True,
        null = True,
     )

    whose = models.ForeignKey(
        User,
        verbose_name='誰の',
        related_name='whose',
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True,
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'