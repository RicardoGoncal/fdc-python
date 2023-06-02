from django.shortcuts import render
from re import template
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from fdcapp.models import PostRequestCloud, PostRequestNetwork
from fdcapp.forms import FormRequestCloud, FormRequestNetwork
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

# Create your views here.
class HomeView(TemplateView):
    template_name = "fdcapp/homepage.html"


class cloud_request(LoginRequiredMixin,View):
    
    def get(self, request):
        form_cloud = FormRequestCloud()
        return render( request, 'fdcapp/cloudform.html', {'form': form_cloud})
    

    def post(self, request):
        form_cloud = FormRequestCloud(request.POST)
        if form_cloud.is_valid():
            form_cloud.save()
            return redirect('homepage')
        
        return render( request, 'fdcapp/cloudform.html', {'form': form_cloud})
    
    
    # template_name = 'fdcapp/cloudform.html'

    # login_url = '/login/'
    # form_class = FormRequestCloud
    # model = PostRequestCloud


class network_request(LoginRequiredMixin, CreateView):
    
    login_url = '/login/'
    form_class = 'xxx'
    model = 'xxxx'


