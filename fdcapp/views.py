from django.shortcuts import render
from re import template
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
# from blog_app.models import Post, Comment
# from blog_app.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class HomeView(TemplateView):
    template_name = "fdcapp/homepage.html"


# Create your views here.
