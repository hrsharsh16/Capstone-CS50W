from django.db import models
from django.contrib.auth.models import AbstractUser
import markdown2

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('reader', 'Reader'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  # Store the article content in Markdown format
    bookmarked_by = models.ManyToManyField(User, related_name='bookmarked_articles', blank=True)


    #convert markdown to html
    def get_rendered_content(self):
        return markdown2.markdown(self.content)

    def __str__(self):
        return f"On {self.created_at}, {self.author} published {self.get_rendered_content()}"
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"