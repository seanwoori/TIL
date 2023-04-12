from django.db import models

class Member(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField()
    age = models.IntegerField()
    country = models.TextField()
    phone = models.TextField(blank=True)
    balance = models.IntegerField()

# 1) 
user1 = Member()
user1.first_name = '철수'
user1.last_name = '김'
user1.country = '서울'
user1.balance = 500
user1.save()
# age가 null값으로 저장되어 오류가 출력됨.

# 2)
user2 = Member('영철', '이', 30, '서울', '010-1234-5678', 1000)
user2.save()
# 멤버 모델에 바로 저장이 불가능함.


# 3)
Member.objects.create('영수', '박', 21, '서울', 2000)
# balance field가 null으로 저장되어 오류가 출력됨.