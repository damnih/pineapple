# from django.contrib import admin
from django.urls import path, include
from . import views
from .views import DepositResultAPIView, DepositProductListView, WishlistToggleAPIView, WishlistListAPIView
from .views import exchange_rate





app_name = 'datas'
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name='savedb'),
    path('deposit-products/', views.deposit_products, name='deposit'),
    path('', views.input_my_data, name='input'),
    # 그럼 이제 나는 이거 그거해야돼, 페이지에서 선택 다 눌러서 전송 버튼 누르면 mine 링크로 가게 하는거 ㅇㅇ 렌더링 되게 하는거 
    path('my_data/', views.filter_by_mine, name='mine'),
    path('api/deposit_results/', DepositResultAPIView.as_view()),
    path('exchange-rate/<str:code>/', exchange_rate),
    path('deposit_results/', DepositProductListView.as_view(), name='deposit-list'),
    path('deposit_results/<int:id>/', views.deposit_result_detail),
    # [NEW] 좋아요 토글 (추가/제거) # POST /api/deposit_results/<int:id>/toggle-like/
    path('deposit_results/<int:id>/toggle-like/', WishlistToggleAPIView.as_view(), name='api-deposit-toggle-like'),
    # [NEW] 내가 좋아요한 상품 목록 조회
    # GET  /api/deposit_results/liked/
    path('deposit-products/liked/', WishlistListAPIView.as_view(), name='api-deposit-liked-list'),
]