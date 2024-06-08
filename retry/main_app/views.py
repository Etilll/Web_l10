from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import Post, Author, Tag
from .forms import PostForm, AuthorForm, CustomUserCreationForm

#from .transfer import prepare_data_for_db

# Create your views here.

class PostCreateView(CreateView):
    model = Post
    author = "author"
    fields = ["post_text", "post_author", "post_tags"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.post_creator = User.objects.get(id=self.request.user.id)
        fields.save()
        setattr(form.instance, self.author, self.request.user)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["post_text", "post_author", "post_tags"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("index")


class PostDeleteView(DeleteView):
    model = Post
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy("index")
    
#####################################
    
class AuthorCreateView(CreateView):
    model = Author
    author = "author"
    fields = ["author_name", "author_desc", "author_birth_place", "author_birth_day", "author_birth_month", "author_birth_year", "author_death_day", "author_death_month", "author_death_year"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author_creator = User.objects.get(id=self.request.user.id)
        fields.save()
        setattr(form.instance, self.author, self.request.user)
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["author_name", "author_desc", "author_birth_place", "author_birth_day", "author_birth_month", "author_birth_year", "author_death_day", "author_death_month", "author_death_year"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("index")


class AuthorDeleteView(DeleteView):
    model = Author
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy("index")
    
##########################################################

class TagCreateView(CreateView):
    model = Tag
    author = "author"
    fields = ["tag_name"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author_creator = User.objects.get(id=self.request.user.id)
        fields.save()
        setattr(form.instance, self.author, self.request.user)
        return super().form_valid(form)


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["tag_name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("index")


class TagDeleteView(DeleteView):
    model = Tag
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy("index")
    
# Create your views here.
def my_posts(request):
    curr_user = request.user.id
    your_posts = Post.objects.filter(post_creator=curr_user).order_by("-post_publish_date")
    template = loader.get_template("main_app/posts.html")
    context = {
        "posts": your_posts,
        "title":"Your posts"
    }
    return HttpResponse(template.render(context=context, request=request))

def authors(request):
    authors = Author.objects.order_by("-author_birth_year")
    template = loader.get_template("main_app/authors.html")
    context = {
        "authors":authors,
        "title":"Authors"
        }
    return HttpResponse(template.render(context=context, request=request))

def author_details(request, author_id):
    author = Author.objects.get(pk=author_id)
    template = loader.get_template("main_app/author.html")
    creator = None
    if author.author_creator == request.user:
        creator = True
    else:
        creator = False
    context = {
        "author":author,
        "creator":creator,
        "title":author.author_name
        }
    return HttpResponse(template.render(context=context, request=request))

def tags(request):
    tags = Tag.objects.order_by("-tag_name")
    template = loader.get_template("main_app/tags.html")
    context = {
        "tags":tags,
        "title":"All tags"
        }
    return HttpResponse(template.render(context=context, request=request))

def tag_details(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    posts = Post.objects.filter(post_tags=tag)
    template = loader.get_template("main_app/tag.html")
    creator = None
    if tag.tag_creator == request.user:
        creator = True
    else:
        creator = False
    context = {
        "tag":tag,
        "posts":posts,
        "creator":creator,
        "title":tag.tag_name
        }
    return HttpResponse(template.render(context=context, request=request))

def index(request):
    last_10_posts = Post.objects.order_by("-post_publish_date")[:10]
    template = loader.get_template("main_app/index.html")
    context = {
        "posts": last_10_posts,
        "title":"Home page"
    }
    return HttpResponse(template.render(context=context, request=request))


def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect(to="index")
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form,
        "title":"Home page"
    }  
    return render(request, 'registration/register.html', context) 