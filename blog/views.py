from blog.models import Post

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    ordering = ['-created_at']

    def get_queryset(self):
        return Post.objects.filter(published=True)



class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'published', 'views_count')
    success_url = reverse_lazy('blog:blog_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview', 'published', 'views_count')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_list')

