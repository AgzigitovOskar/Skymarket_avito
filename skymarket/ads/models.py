from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.CharField(max_length=1000, null=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, max_length=1500)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id}: {self.title} - {self.price}"


class Comment(models.Model):
    text = models.CharField(max_length=1000, null=False, blank=False )
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey('ads.Ad', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']

