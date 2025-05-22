# from django.contrib import admin
from django.urls import path, include
from . import views
from .views import DepositResultAPIView

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name='savedb'),
    path('deposit-products/', views.deposit_products, name='deposit'),
    path('', views.input_my_data, name='input'),
    # 그럼 이제 나는 이거 그거해야돼, 페이지에서 선택 다 눌러서 전송 버튼 누르면 mine 링크로 가게 하는거 ㅇㅇ 렌더링 되게 하는거 
    path('my_data/', views.filter_by_mine, name='mine'),
    # path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='depositopt'),
    # path('datas/', include('datas.urls')),
    # path('admin/', admin.site.urls),
    path('api/deposit_results/', DepositResultAPIView.as_view()),
]
