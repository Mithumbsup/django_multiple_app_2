from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, Comment, User

from django.http import HttpResponse
from .forms import PostForm, CommentForm, CreateUserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import permission_required,login_required
from django.views import View

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


def main(request):
    return render(request,'blog/IT.html')

def post_list(request):
    posts = Post.objects.all()

    return render(request,'blog/post_list.html',{"posts":posts})



#create
def post_create(request):
    if request.method == 'POST':
        Post_form = PostForm(request.POST)

        if Post_form.is_valid():
            post = Post_form.save()
            return HttpResponse('생성완료')
        
    else:
        Post_form = PostForm()

    return render(request, 'blog/post_create.html', {
        'Post_form':Post_form,
    }) 



def comment_create(request, pk):
    post =  get_object_or_404(Post, id = pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit = False)
        comment.post = post
        comment = form.save()
    
    return redirect(post)



#read
def post_read(request,pk):
    post = get_object_or_404(Post, id=pk)
    form = CommentForm()
    return render(request,'blog/post_read.html',{
        'post':post,
        'form':form,
        })


#update
@permission_required('can_add_log_entry')
def post_edit(request, pk):
    post = get_object_or_404(Post, id = pk)

    if request.method =='POST':
        Post_form = PostForm(request.POST, instance = post)

        if Post_form.is_valid():
            post = Post_form.save()
            return HttpResponse('수정완료')
    else:
        Post_form = PostForm(instance = post)
    
    return render(request, 'blog/post_create.html',{
        'Post_form':Post_form,
    })


#delete
def post_delete(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.delete()
    return render(request, 'blog/main.html')

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm 
    success_url = reverse_lazy('blog:create_user_done') 

class RegisteredView(TemplateView): 
    template_name = 'registration/login_done.html' 

def permission_denied(request):
    return render(request, 'registration/permission_denied.html',{
    })



def profile(request):
    if not request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
    else:
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password, 'is_authenticated': request.user.is_authenticated}
    return render(request, 'profile.html', context={'data': data}) 
    