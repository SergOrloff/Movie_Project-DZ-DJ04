from django.db import models

class Film(models.Model):
    objects = None
    title = models.CharField("Название фильма", max_length=100)
    description = models.TextField("Описание фильма")
    review = models.TextField("Отзыв")
    image = models.ImageField("Обложка фильма", upload_to='film_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
