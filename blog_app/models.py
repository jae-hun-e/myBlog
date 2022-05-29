# blog 글에 해당하는 객체 (Table만드는 것임 - ORM)
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')  # 업로드 여부 선택, 업로드시 경로 media/blog_photo에 추가됨
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
    # on_delete : Post 가 참고하고 있는 blog 가 삭제되면 post 의 comment 도 같이 삭제됨
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
