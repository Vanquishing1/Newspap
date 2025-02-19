from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filters import PostFilter
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(type=Post.NEWS).order_by('-created_at')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_count'] = self.get_queryset().count()
        return context

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

class NewsSearchView(FilterView):
        model = Post
        template_name = 'news/news_search.html'
        context_object_name = 'news'
        filterset_class = PostFilter
        paginate_by = 10


class NewsCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.NEWS
        return super().form_valid(form)

class NewsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/news_form.html'

class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.ARTICLE
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/news_form.html'

class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news_list')

class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
