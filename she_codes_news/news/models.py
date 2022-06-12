from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.URLField(max_length=200)


class Author(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    author = user.name

    def get_absolute_url(self):
        return reverse("author", kwargs={'pk': self.pk})

    def __str__(self):
        return self.author.username
