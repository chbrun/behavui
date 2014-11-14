from django.views import generic

from .models import Project


# Create your views here.
class IndexView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
