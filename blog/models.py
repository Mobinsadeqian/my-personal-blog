from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
# ... (کلاس Post) ...

class Comment(models.Model):
    # باید post (حرف کوچک) باشد
    post = models.ForeignKey( # ⚠️ این فیلد باید post با حرف کوچک باشد
        'Post', 
        on_delete=models.CASCADE, 
        related_name='comments' # ⬅️ این نام باید دقیقا "comments" باشد
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False) # بهتر است پیش فرض False باشد تا ادمین تایید کند

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        # اینجا هم باید self.post باشد (با حرف کوچک)
        return f'Comment by {self.name} on {self.post}'    
