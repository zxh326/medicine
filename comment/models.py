from django.db import models
from disease.models import Disease
from user.models import User
# Create your models here.


class Comment(models.Model):
    """Model definition for Comment."""
    # TODO: Define fields here

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['comment_time']

    def __str__(self):
        """Unicode representation of Comment."""
        return self.content[:10]
    
    topic = models.ForeignKey(Disease, on_delete=models.CASCADE)
    content = models.TextField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_from')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_to', null=True, blank=True)
    comment_time = models.DateTimeField(auto_now_add=True)
