from django.urls import path, include
from .views import ArticleCreateView
from articles import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list),
    path('create/', views.ArticleCreateView.as_view()),
    path('<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.comment_create),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
]



