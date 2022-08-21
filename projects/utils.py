from .models import Project


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    projects = Project.objects.filter(title__icontains=search_query)
    return projects, search_query
