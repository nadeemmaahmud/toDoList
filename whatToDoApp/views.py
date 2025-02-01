from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from . import models
from . import forms

# Create your views here.

class TaskHome(ListView):
    model = models.Task
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskCreate(LoginRequiredMixin, CreateView):
    form_class = forms.CreateForm
    template_name = 'create_edit.html'
    success_url = reverse_lazy('home')
    extra_context = {'create' : True}

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully...')
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    form_class = forms.UpdateForm
    model = models.Task
    pk_url_kwarg = 'id'
    template_name = 'create_edit.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully...')
        return super().form_valid(form)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = models.Task
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Task deleted successfully...')
        return super().form_valid(form)

def create_user(request):
    if request.method == 'POST':
        form = forms.CreateUser(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully...')
            return redirect('profile')

    else:
        form = forms.CreateUser()

    return render(request, 'login_register.html', {'form': form, 'create' : True})


def login_user(request):
    if request.method == 'POST':
        form = forms.UserLogin(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'User logged In successfully...')
            return redirect('home')
        else:
            messages.error(request, "Credentials isn't matched...")

    else:
        form = forms.UserLogin()

    return render(request, 'login_register.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'User logged out successfully...')
    return redirect('home')

class Profile(LoginRequiredMixin, ListView):
    model = models.Task
    template_name = 'profile.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return models.Task.objects.filter(user=self.request.user)