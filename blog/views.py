from django.shortcuts import render

from django.views.generic import ListView    # ListViewはdjango.views.genericに定義されているので、インポート
from .models import Blog   # Blogモデルに関連付けるため、インポート
# クラスベース汎用ビュー
# トップページ
class BlogListView(ListView):  # BlogListViewクラスを定義し、ListViewを継承
  model = Blog   # BlogListViewクラスとBlogモデルを関連付ける
