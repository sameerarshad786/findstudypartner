from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, BioUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'title': 'Register',
    }
    return render(request, 'users/register.html' , context)

@login_required
def userprofile(request, pk):
    user = get_object_or_404(User, id=pk)
    rooms = user.room_set.all().order_by('-date_posted')
    
    context = {
        'user': user,
        'rooms': rooms,
        'title': 'profile',
    }
    return render(request, 'users/profile.html', context)

@login_required
def editprofile(request, pk):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        b_form = BioUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid() and b_form.is_valid():
            p_form.save()
            u_form.save()
            b_form.save()
            return redirect('user-profile', pk=pk)
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        b_form = BioUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
        'u_form': u_form,
        'b_form': b_form,
        'title': 'Edit Profile',
    }
    return render(request, 'users/editprofile.html', context)