from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class NewsCategory(models.Model):

    title = models.CharField(max_length=100)
    title_slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    class Meta:
        abstract = True


class News(DateTimeModel):

    title = models.CharField(max_length=1000)
    description = models.TextField()
    title_slug = models.SlugField(blank=True)
    relavent_url = models.URLField(
        null=True, blank=True)
    relavent_image = models.ImageField(
        null=True, blank=True)
    author = models.CharField(
        default='Not Available', max_length=100)
    date = models.DateTimeField(
        null=True, blank=True)
    category = models.ForeignKey(
        NewsCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        )
    notified_by = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class NewsSource(models.Model):
    
    url = models.URLField()
    api_key = models.CharField(
        max_length=100, null=True, blank=True
        )

    def __str__(self):
        return self.url


class Notification(DateTimeModel):

    url = models.URLField()
    is_seen = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
