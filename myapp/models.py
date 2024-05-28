from django.db import models

class CodeSnippet(models.Model):
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.code