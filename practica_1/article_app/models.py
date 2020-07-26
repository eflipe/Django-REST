from django.db import models


class Author(models.Model):
    # TODO: Define fields here
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Article(models.Model):
    # TODO: Define fields here
    title = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
