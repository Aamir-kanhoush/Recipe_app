from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RecipeListView, RecipeDetailView, RecipeDelete, RegisterView, RecipeCreateView, RecipeUpdateView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('recipes/create/', RecipeCreateView.as_view(), name='create_recipe'),
    path('recipes/list_view/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/detail/<int:pk>/',RecipeDetailView.as_view(), name='recipe_detail'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html',next_page='recipe_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
]