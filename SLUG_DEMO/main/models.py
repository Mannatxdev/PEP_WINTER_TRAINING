from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])
