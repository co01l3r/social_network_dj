from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {'project': projectObj, 'tags': tags}
    return render(request, 'projects/single-project.html', context)


def create_project(request):
    """
    check if data are POST, take POST values from create form, validate them and if they are ok:
    save them into db and redirect user back to main view
    """
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def update_project(request, pk):
    """
    take the project model which has to match with model form and prefill all fields with project
    data by pk, check if new data are valid and continue to save them into db under the same pk,
    using the same template as create_project and redirect the user back to main view
    """
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def delete_project(request, pk):
    """
    take the project model which has to match with model form and proceed to render delete
    template from db and redirect user back to main view
    """
    project = Project.objects.get(id=pk)
    context = {'object': project}

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'projects/delete_template.html', context)
