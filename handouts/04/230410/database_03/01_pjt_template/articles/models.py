from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delelte=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

class Comment(models.Model):
    '''
    article과의 관계에 대한 필드 - ForeignKey(무엇이랑 연결이 되어있는데?, 지울 때의 디폴트 행위를 입력)
    '''
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # related_name 이라는 변수로 comment_set 명을 변환할 수 있음.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content