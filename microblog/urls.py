"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from blog.views import BlogListView
from blog.views import BlogDetailView
from blog.views import BlogCreateView, BlogUpdateView, BlogDeleteView
# リクエスト → url.py  → ビュー → テンプレート → レスポンス
urlpatterns = [
    # path('<URL>', views(関数), ニックネーム),
    path('', BlogListView.as_view(), name="index"),   # トップページ
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),  #詳細表示ページ
    path('<int:pk>/update', BlogUpdateView.as_view(), name="update"), # 更新
    path('<int:pk>/delete', BlogDeleteView.as_view(), name="delete"), # 削除
    # int(整数)をpk(primary key、変数)に代入するような設定（localhost:8000/ココの数字のこと）

    path('create', BlogCreateView.as_view(), name="create"),

    path('login', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),

    path('admin/', admin.site.urls),
]
