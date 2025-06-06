from django.urls import path, include
from .views import SignupView, LoginView, UserView, UserDetailView
from articles import views

app_name = 'accounts'
urlpatterns = [
    # path('', UserCreateView.as_view()),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserView.as_view(), name='my-detail'),
    path('<str:username>/', UserDetailView.as_view(), name='user-detail'),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('<int:article_pk>/comments/', views.comment_create),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
]



