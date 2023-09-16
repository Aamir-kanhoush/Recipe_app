from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.urls import reverse_lazy
from .models import recipe
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from .forms import RecipeForm
from django.contrib.auth.views import LogoutView
# Create your views here.

class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recipe_form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = recipe
    form_class = RecipeForm
    template_name = 'recipe_edit.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})


class RecipeListView(LoginRequiredMixin, ListView):
    model = recipe
    context_object_name='recipe'
    template_name = 'recipe_list.html'
    #ordering = ['-updated_at']

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('-----------------')
        print(context)
        print('-----------------')
        context['recipe'] = context['recipe'].filter(user=self.request.user)
        print(context)
        return context
    
    def get_success_url(self):
        return reverse_lazy('recipe_list', kwargs={'pk': self.object.pk})



class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = recipe
    context_object_name='recipe'
    template_name = 'recipe_detail.html'
    
    
    
class RecipeDetail(LoginRequiredMixin, generic.DetailView):
    model = recipe

class RecipeDelete(LoginRequiredMixin, generic.DeleteView):
    model = recipe
    success_url = reverse_lazy('Recipes:recipe')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('recipe_list')
        return render(request, self.template_name, {'form': form})
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')