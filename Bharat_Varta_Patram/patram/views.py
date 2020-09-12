from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, PostComment
from .forms import CreatePostComment
from patram.templatetags import extras

def home(request):
    content = {
        'posts': Post.objects.all().order_by('-date'),
        'title': 'Home',

    }
    return render(request, 'patram/home.html', content)

def postDetail(request, pk):
    post = Post.objects.filter(pk=pk).first()
    title = post.title
    if request.method == 'POST':
        if not request.user.is_authenticated:
            redir = 'http://127.0.0.1:8000/login?next='+request.path
            return redirect(redir)
        form = CreatePostComment(request.POST)
        
        if form.is_valid():
            print('00099900')
            user = request.user
            comment = form.cleaned_data['comment']
            if form.cleaned_data['parent'] is not None:
                newcomment = PostComment(user=user, post=post,comment=comment, parent = form.cleaned_data['parent'] )
            else:
                newcomment = PostComment(user=user, post=post,comment=comment)
            newcomment.save()
            messages.success(request, f'Comment successfully posted!')
        else:
            print('form',form)
            print('failed-----------------------------------')
    else:
        form = CreatePostComment()
    
    comment = PostComment.objects.filter(post=post, parent=None)
    replies = PostComment.objects.filter(post=post).exclude(parent=None)
    replies_dict = {}
    for reply in replies:
        if reply.parent.id not in replies_dict:
            replies_dict[reply.parent.id] = [reply]
        else:
            replies_dict[reply.parent.id].append(reply)

    print(replies_dict)
    content = {'post':post, 'comments':comment, 'replies_dict':replies_dict, 'title':title, 'form':form}
    return render(request, 'patram/post_detail.html', content)

class PostListView(ListView):
    model = Post
    template_name = 'patram/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'patram/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','description','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blogs/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = PostComment
    template_name = 'patram/post_detail.html'
    fields = ['comment']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.get_object()
        return super().form_valid(form)


