from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Mark(models.Model):
    mark_value = models.CharField(max_length=20, choices=[
        (1, 'Like'),
        (2, 'Dislike')
    ])
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.mark_value