from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название', null=True)
    anons = models.CharField(max_length=201, verbose_name='Анонс', null=True)
    content = models.TextField(verbose_name='Контент', null=True)
    date = models.DateTimeField(verbose_name='Cоздан', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
