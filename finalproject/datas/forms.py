from django import forms
from .models import ItemOptions


# 비교 대상이 되는 모델(Item)을 import

# DB에 저장할 게 아니면 걍 일반 Form을 써줘도 됨 
# class CompareForm(forms.ModelForm):
class MyDataForm(forms.Form):
    # 내가 새로 지정할 옵션들 (DB와 무관)
    
    DESTINATION_CHOICES = [
        ('일본', '일본'),
        ('중국', '중국'),
        ('대만', '대만'),
        ('베트남', '베트남'),
        ('태국', '태국'),
        ('그 외 동남아시아', '그 외 동남아시아'),
        ('서남아시아', '서남아시아'),
        ('유럽', '유럽'),
        ('북아메리카', '북아메리카'),
        ('남아메리카', '남아메리카'),
        ('호주', '호주'),
        ('그 외', '그 외'),
    ]

    SCHEDULE_CHOICES = [
        ('1', '1개월 후'),
        ('3', '3개월 후'),
        ('6', '6개월 후'),
        ('12', '1년 후'),
        ('24', '2년 후'),
    ]


    # 문자열이지만, coerce=int 로 int로 변환해서 비교할 수 있게 함
    destination = forms.ChoiceField(
        choices=DESTINATION_CHOICES,
        # coerce=int,
        # label="여행지",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    schedule = forms.TypedChoiceField(
        choices=SCHEDULE_CHOICES,
        coerce=int,
        # label="여행 일정",
        widget=forms.Select(attrs={'class': 'form-select'})
        # form-select라는 이름의 클래스를 지정해줘서(속성을 정의) 나중에 CSS 스타일링할 때 용이하게 해준거임!!! 
    )

    budget = forms.IntegerField(label="예산(원)", min_value=0, widget=forms.NumberInput(attrs={'placeholder':'단위: 만 원'}))



