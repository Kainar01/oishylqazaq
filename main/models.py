import datetime
from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.datetime.now)
    ordering = ['-created']

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    full_name = models.CharField(max_length=300)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", verbose_name="Categories", on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="")
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, verbose_name="Author", on_delete=models.CASCADE)
    audio = models.FileField(upload_to="audio/", max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="thumbnail/", blank=True, null=True)
    released = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-uploaded']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
