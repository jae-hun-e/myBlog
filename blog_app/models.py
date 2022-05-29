# blog 글에 해당하는 객체 (Table만드는 것임 - ORM)
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')  # 업로드 여부 선택, 업로드시 경로 media/blog_photo에 추가됨
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
