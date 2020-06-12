from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView    # ListViewはdjango.views.genericに定義されているので、インポート
from django.views.generic import DetailView  # 詳細表示ページ
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Blog   # Blogモデルに関連付けるため、インポート

from .forms import BlogForm

# クラスベース汎用ビュー
# トップページ
class BlogListView(ListView):  # BlogListViewクラスを定義し、ListViewを継承
  model = Blog   # BlogListViewクラスとBlogモデルを関連付ける
  context_object_name = "blogs"
  paginate_by = 3

#詳細表示ページ
class BlogDetailView(DetailView):
  model = Blog
  context_object_name = "blog"

class BlogCreateView(CreateView):
  model = Blog
  form_class = BlogForm
  success_url = reverse_lazy("index")
  template_name = "blog/blog_create_form.html"

  def form_valid(self, form):
    messages.success(self.request, "保存しました")
    return super().form_valid(form)

  def form_invalid(self, form):
    messages.error(self.request, "保存に失敗しました")
    return super().form_invalid(form)

class BlogUpdateView(UpdateView):
  model = Blog
  form_class = BlogForm
  template_name = "blog/blog_update_form.html"

  def get_success_url(self):
    blog_pk = self.kwargs["pk"]
    url = reverse_lazy("detail", kwargs={"pk":blog_pk})
    return url
  
  def form_valid(self, form):
    messages.success(self.request, "更新されました")
    return super().form_valid(form)

  def form_invalid(self, form):
    messages.error(self.request, "更新に失敗しました")
    return super().form_invalid(form)

class BlogDeleteView(DeleteView):
  model = Blog
  success_url = reverse_lazy("index")

  def delete(self, request, *args, **kwargs):
    messages.error(self.request, "削除しました")
    return super().delete(request, *args, **kwargs)
