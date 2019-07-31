from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Group
from .form import GroupForm


def index(request): 
    groups = Group.objects.all()
    return render(request, 'group/index.html', {'groups' : groups})

def create(request): 
    if request.method == "POST" : 
        form = GroupForm(request.POST) 
        if form.is_valid() : 
            group = form.save(commit=False)
            group.save()
            return redirect('detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'group/create.html', {'form' : form})    

def delete(request, pk): 
    if request.method == 'POST' : 
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return redirect('/group')
    return HttpResponse('잘못된 접근')

def edit(request, pk): 
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST' : 
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('detail', pk=group.pk) 
    else:
        form = GroupForm(instance=group)
    return render(request, 'group/edit.html', {'form' : form})     

def detail(request, pk): 
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'group/detail.html', {'group' : group})     