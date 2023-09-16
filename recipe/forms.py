from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import recipe
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('recipe_list')
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your account has been created!')
        return response

class RecipeForm(forms.ModelForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = recipe
        fields = ['title', 'description', 'ingredients', 'directions', 'meal_type', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'ingredients': forms.Textarea(attrs={'rows': 6}),
            'directions': forms.Textarea(attrs={'rows': 15}),
        }
        labels = {
            'title': 'Title*',
            'description': 'Description',
            'ingredients': 'Ingredients*',
            'directions': 'Directions*',
            'meal_type': 'Meal Type',
            'image': 'Image',
        }
        required = {
            'title': True,
            'description': False,
            'ingredients': True,
            'directions': True,
            'meal_type': False,
            'image': False,
        }