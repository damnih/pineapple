from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드 
    kor_co_nm = models.TextField() # 금융 회사 코드 
    fin_prdt_nm = models.TextField() # 금융 상품명
    etc_note = models.TextField() # 기타 유의사항 
    join_deny = models.IntegerField() # 가입 제한 
    join_member = models.TextField() # 가입 대상
    join_way = models.TextField() # 가입 방법
    spcl_cnd = models.TextField() # 우대조건 
    # subscribes = models.ManyToManyField(User, related_name='subs_list')
    # likes = models.ManyToManyField(User, related_name='likes_list')


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='options') # 어떤 상품의 옵션인지 외래키 
    fin_prdt_cd = models.TextField() # 금융상품 코드 
    intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명
    intr_rate = models.FloatField() # 저축 금리 
    intr_rate2 = models.FloatField() # 저축 우대금리(최고)
    save_trm = models.IntegerField() # 저축 기간

    def __str__(self):
        return f"{self.fin_prdt_cd} - {self.save_trm}개월"


class ItemOptions(models.Model):
    pass 


