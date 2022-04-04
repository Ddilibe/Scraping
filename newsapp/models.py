from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length = 400)
    slug = models.SlugField(max_length = 600)
    image_url = models.URLField()
    body = models.TextField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
        
class Comment(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = True)

    class Meta:
        ordering = ['publish', ]
        
        
    def __str__(self):
        return f"Commented by {self.name}"
