from django.db import models


class Ad(models.Model):
    # objects = None
    title = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name = 'Отзыв'
    #     verbose_name_plural = 'Отзывы'
    #     ordering = ['-created_at']
    #
    # def __str__(self):
    #     return self.text



