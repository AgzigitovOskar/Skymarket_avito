from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='Автор')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.CharField(max_length=2000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='ad_images/', blank=True, null=True, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['created_at']


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



