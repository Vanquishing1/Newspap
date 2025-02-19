from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def become_author(request):
    authors_group, _ = Group.objects.get_or_create(name='authors')
    if request.user not in authors_group.user_set.all():
        request.user.groups.add(authors_group)
    return redirect('profile')

